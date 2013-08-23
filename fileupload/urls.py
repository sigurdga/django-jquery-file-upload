from django.conf.urls import patterns, url
from fileupload.views import BasicVersionCreateView, PictureCreateView, PictureDeleteView

urlpatterns = patterns('',
    (r'^basic/$', BasicVersionCreateView.as_view(), {}, 'upload-basic'),
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
    url(r'^view/$', 'fileupload.views.PictureListView', name='upload-view'),
)



