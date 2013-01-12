import os
from settings import *

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_PATH, 'wines.db'), # path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LOCAL_DEVELOPMENT = True

#MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

#MEDIA_URL = ''
#ADMIN_PREFIX_MEDIA = '/media/admin/'
