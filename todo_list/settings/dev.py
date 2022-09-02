from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-70wpoe5rz7x&^*y*ndtaye2t@%0n3hf=5$h_r$24_b_o7%mdxx'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'todo_list',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'engineer1900'
    }
}
