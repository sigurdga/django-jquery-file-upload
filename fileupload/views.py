from fileupload.models import Picture
from django.views.generic import CreateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings
import re

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

def orderName(name):
    name = re.sub (r'^.*/', '', name)
    if len(name)>20:
        return name[:10] + "..." + name[-7:]
    else:
        return name

class PictureCreateView(CreateView):
    model = Picture

    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        files = [{
            'url': self.object.file.url,
            'name': orderName(f.name),
            "type": "image/png",
            'thumbnailUrl': self.object.file.url,
            'size': f.size,
            'deleteUrl': reverse('upload-delete', args=[self.object.id]),
            'deleteType': "DELETE",
            }]
        data = {"files": files}
        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

class BasicVersionCreateView(PictureCreateView):
#    model = Picture
    template_name_suffix = '_basic_form'
    
class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        self.object.delete()
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/upload/new')

def PictureListView(request):
    files = []
    for obj in Picture.objects.all():
        files += [{
        'name': orderName(obj.file.name),
        'size': obj.file.size,
        'url': obj.file.url,
        'thumbnailUrl': obj.file.url,
        'deleteUrl': reverse('upload-delete', args=[obj.id]),
        'deleteType': "DELETE"
        }]
    data = {"files": files}
    response = JSONResponse(data, {}, response_mimetype(request))
    response['Content-Disposition'] = 'inline; filename=files.json'
    return response

class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)
