from .basic import *

ENV_MODE = 'dev'
DEBUG = True
WSGI_APPLICATION = 'settings.wsgi_dev.application'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3307,
        'NAME': 'admin',
        'USER': 'root',
        'PASSWORD': '123456'
    },
    'content': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3307,
        'NAME': '233cafe',
        'USER': 'root',
        'PASSWORD': '123456'
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

ADMIN_PATH = 'admin'
