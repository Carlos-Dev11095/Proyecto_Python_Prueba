"""
WSGI config for prueba project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

path = os.path.expanduser('~/Charliedev-11095/prueba')
if path not in sys.path:
    sys.path.insert(0,path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba.settings')
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())
