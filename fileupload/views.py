from fileupload.models import Picture
from django.views.generic import CreateView

from django.http import HttpResponse
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.utils import simplejson

from django.conf import settings

class PictureCreateView(CreateView):
    model = Picture

    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('file')
        data = [{'name': f.name, 'url': settings.MEDIA_URL + "pictures/" + f.name, 'thumbnail_url': settings.MEDIA_URL + "pictures/" + f.name, 'delete_url': "index.html", 'delete_type': "DELETE"}]
        return JSONResponse(data)

class JSONResponse(HttpResponse):
    """ JSON response class """
    def __init__(self,content='',json_opts={},mimetype="application/json",*args,**kwargs):
        """
        This returns a object that we send as json content using
        samklang.core.encoders.serialize, that is a wrapper to simplejson.dumps
        method using a custom class to force_unicode for lazy translatons. Put
        your options to serialize in json_opts, other options are used by
        response.
        """
        if content:
            content = serialize(content,**json_opts)
        else:
            content = serialize([],**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)

def serialize(obj,*args,**kwargs):
    """ A wrapper for simplejson.dumps with defaults as:
        ensure_ascii=False
        cls=LazyJSONEncoder

        All arguments can be added via kwargs
    """

    kwargs['ensure_ascii'] = kwargs.get('ensure_ascii',False)
    kwargs['cls'] = kwargs.get('cls',LazyEncoder)

    return simplejson.dumps(obj,*args,**kwargs)

class LazyEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return super(LazyEncoder, self).default(obj)

