DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'test',
        'OPTIONS': {'OPERATIONS': {}},
        'PORT': '27017',
    },
    'other': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'test2',
        'PORT': '27017',
},
}

SERIALIZATION_MODULES = {'json': 'settings.serializer'}

SECRET_KEY = 'super secret'

try:
    from local_settings import *
except ImportError:
    pass
