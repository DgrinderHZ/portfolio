from .settings import *
import os
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

debug_options = os.environ.get('DEBUG').lower()
if debug_options == 'true':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['zeekzone.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}



