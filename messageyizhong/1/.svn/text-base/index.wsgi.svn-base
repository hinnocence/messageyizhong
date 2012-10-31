
import os
import django.core.handlers.wsgi
import sys
import sae

sys.path.append('messageyizhong')

os.environ['DJANGO_SETTINGS_MODULE'] = 'messageyizhong.settings'

application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())

