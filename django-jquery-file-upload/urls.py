from django.urls import include, path
from django.http import HttpResponseRedirect
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', lambda x: HttpResponseRedirect('/upload/new/')),
    path('upload/', include('fileupload.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
