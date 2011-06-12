from django.conf.urls.defaults import *
from fileupload.views import PictureCreateView, PictureDeleteView

urlpatterns = patterns('',
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    (r'^delete/(?P<slug>.+)$', PictureDeleteView.as_view(), {}, 'upload-delete'),
)

