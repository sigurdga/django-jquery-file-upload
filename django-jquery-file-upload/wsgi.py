"""
WSGI config for django-jquery-file-upload project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-jquery-file-upload.settings")

application = get_wsgi_application()
