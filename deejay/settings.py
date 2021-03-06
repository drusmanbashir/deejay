import sys
from os.path import abspath, basename, dirname, join, normpath


########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Site name.
SITE_NAME = basename(DJANGO_ROOT)

# Absolute filesystyesem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('usman', 'drusmanbashir@yahoo.com'),
)
sys.path.append(SITE_ROOT)
sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
sys.path.append(normpath(join(DJANGO_ROOT, 'libs')))

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pacsdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'usman',
        'PASSWORD': 'barrium',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },
    'theory': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'rad',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'usman',
        'PASSWORD': 'barrium',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',
    }
            }
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

# URL prefix for static files.
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.DMID
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files.
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'assets')),
)

# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION
# Make this unique, and don't share it with anybody.
SECRET_KEY = '5*f&amp;j^drul=fnds^jx1-e(d^mmqh7cjq0=ygao!p$r!7^ph1g4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'django.contrib.staticfiles',
)

ROOT_URLCONF = 'deejay.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'deejay.wsgi.application'


INSTALLED_APPS = (
    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'blog',
    #'editor',
    'django.contrib.flatpages',
    'django.contrib.syndication',
    'PIL',
    'django_markdown',
    'disqus',
    'numpy',
    #'south',
    'dicom',
    'pacscon',
    'knowledge',
    #'trialApp',
  #  'viewer',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#ROUTERS = normpath(join(DJANGO_ROOT, 'deejay/pacsrouter'))
#DATABASE_ROUTERS = ['pacscon.pacsrouter.pacsRouter', 'pacscon.pacsrouter.trialRouter', ]

SC_DICOM_SERVER = 'localhost'
SC_DICOM_PORT = 11112

SC_WADO_SERVER = 'localhost'
SC_WADO_PORT = 8080
SC_WADO_PATH = 'wado'
AET = 'DCM4CHEE'
