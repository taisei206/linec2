from .settings_common import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

STATIC_ROOT = '/usr/share/nginx/html/static'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,


    'loggers': {
        'django': {
        'handlers': ['file'],
        'level': 'INFO',
        },

        'config': {
        'handlers': ['file'],
        'level': 'INFO',
        },
    },


    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },


    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
