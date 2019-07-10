# Site-specific configuration settings for Review Board
# Definitions of these settings can be found at
# http://docs.djangoproject.com/en/dev/ref/settings/

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reviewboarddb',
        'USER': 'root',
        'PASSWORD': 'Techo2@123',
        'HOST': 'localhost',
        'PORT': '',
    },
}

# Unique secret key. Don't share this with anybody.
SECRET_KEY = '2*0z#$k&2!fd7-1#%n0s+a*^0$vrwl&d__y$k$l+09w4=*e@)$'

# Cache backend settings.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    },
}

# Extra site information.
SITE_ID = 1
SITE_ROOT = '/'
FORCE_SCRIPT_NAME = ''
DEBUG = False
ALLOWED_HOSTS = ['sampledomain.com']
