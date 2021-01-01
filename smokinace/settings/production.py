from .base import *
from dotenv import load_dotenv

load_dotenv()
if os.environ.get('DEBUG_MODE') == 'True':
    DEBUG = True
elif os.environ.get('DEBUG_MODE') == 'False':
    DEBUG = False

ALLOWED_HOSTS = ['*']
# 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USERNAME'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'ATOMIC_REQUESTS': True,
        'HOST': str(os.environ.get('DATABASE_HOST')),
        'PORT': int(os.environ.get('DATABASE_PORT'))
    }
}


NOTIFICATION_MESSAGE_TEMPLATES = {
    "START_TRIP_NOTIFICATION_MESSAGE":
    os.environ.get('START_TRIP_NOTIFICATION_MESSAGE'),
    "END_TRIP_NOTIFICATION_MESSAGE":
    os.environ.get('END_TRIP_NOTIFICATION_MESSAGE'),
    "TRIP_NOTIFICATION_SUBJECT":
    os.environ.get('TRIP_NOTIFICATION_SUBJECT')
}

SERVICE_URLS = {
    'shared_service': os.environ.get('TRANSFER_PROTOCOL') + '://' + os.environ.get('SHARED_SERVICE') + os.environ.get('API_VERSION')
}