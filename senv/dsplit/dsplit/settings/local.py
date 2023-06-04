from .base import * 
from decouple import config
DEBUG = config('DEBUG', cast=bool,default=True)
SECRET_KEY = config('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DEBUG = True



ALLOWED_HOSTS = ["127.0.0.1"] 

INSTALLED_APPS += (
   
    
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
