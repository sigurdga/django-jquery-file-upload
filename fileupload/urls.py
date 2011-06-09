from django.conf.urls.defaults import *
from fileupload.views import PictureCreateView

urlpatterns = patterns('',
    (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
)

