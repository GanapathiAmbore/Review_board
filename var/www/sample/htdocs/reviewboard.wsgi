import __main__
__main__.__requires__ = ['ReviewBoard']
import pkg_resources

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = "reviewboard.settings"
os.environ['PYTHON_EGG_CACHE'] = "/var/www/sample/tmp/egg_cache"
os.environ['HOME'] = "/var/www/sample/data"
os.environ['PYTHONPATH'] = '/var/www/sample/conf:' + os.environ.get('PYTHONPATH', '')

sys.path = ['/var/www/sample/conf'] + sys.path

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
