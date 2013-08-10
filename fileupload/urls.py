from django.conf.urls.defaults import patterns, url
from fileupload.views import PictureCreateView, PictureDeleteView

urlpatterns = patterns('',
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
    url(r'^view/$', 'fileupload.views.PictureListView', name='upload-view'),
)



