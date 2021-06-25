"""
WSGI config for crawler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crawler.settings')

application = get_wsgi_application()
from whitenoise import WhiteNoise
from my_project import MyWSGIApp
application = MyWSGIApp()
application = WhiteNoise(application, root='/web/crawler')
application.add_files('/web/crawler/templates/', prefix='more-files/')
application.add_files('/web/crawler/trans/templates/', prefix='more-files/')