from django.conf.urls import patterns, url
from fileupload.views import BasicVersionCreateView, BasicPlusVersionCreateView, PictureCreateView, AngularVersionCreateView, jQueryVersionCreateView, PictureDeleteView

urlpatterns = patterns('',
    (r'^basic/$', BasicVersionCreateView.as_view(), {}, 'upload-basic'),
    (r'^basic/plus/$', BasicPlusVersionCreateView.as_view(), {}, 'upload-basic-plus'),
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^angular/$', AngularVersionCreateView.as_view(), {}, 'upload-angular'),
    (r'^jquery-ui/$', jQueryVersionCreateView.as_view(), {}, 'upload-jquery'),
    (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
    url(r'^view/$', 'fileupload.views.PictureListView', name='upload-view'),
)



