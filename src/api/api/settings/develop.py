from .production import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'obhijan_jobs',
        'HOST': 'localhost',
        'USER': 'shetu',
        'PORT': '5432',
        'PASSWORD': 'shetu2153'
    }
}
