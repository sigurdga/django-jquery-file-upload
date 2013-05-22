from django.conf.urls import patterns
from fileupload.views import PictureCreateView, PictureDeleteView

urlpatterns = patterns('',
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
)

