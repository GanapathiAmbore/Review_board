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
SECRET_KEY = '#6s9d6(r1p8^@5^a-b^n(a(q=2xi)ulp8&i5-rez1+mr&e5av7'

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
ALLOWED_HOSTS = ['*']
