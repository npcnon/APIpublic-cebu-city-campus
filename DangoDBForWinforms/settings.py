from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'jcPDihGiqU5n7LxWruTFj5m6Jjt9d5TDBL60tdSZagWkchF3RGUuhciezNLJteRDad4')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com', 'localhost']



CORS_ALLOW_CREDENTIALS = True

# Email Configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'afkmhafric@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'pqnc gcie kact pwrd')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_cron',
    'rest_framework',
    'users',
    'DangoDBApp',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DangoDBForWinforms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DangoDBForWinforms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#  Microsoft SQL Server
# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',  
#         'NAME': 'EnrollmentSystemDB', 
#         'HOST': 'DESKTOP-GVSR043\\SQLEXPRESS',  
#         'PORT': '',  
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#             'Encrypt': 'no',
#         },
#     }
# }




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'u286307273_portal',
#         'USER': 'u286307273_portal',
#         'PASSWORD': 'W5Cn6Q>+:l',
#         'HOST':'srv1417.hstgr.io',
#         'PORT':'3306',
#     },
#      'secondary': { 
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'AnotherDatabase',
#         'USER': 'root',
#         'PASSWORD': 'qwerty',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     },
# }

#SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
CRON_CLASSES = [
    "DangoDBApp.cron.FetchAPIDataCronJob",
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Singapore'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

CORS_ALLOW_HEADERS = [
    'authorization',  
    'content-type',
]

# Optionally specify allowed origins if CORS_ORIGIN_ALLOW_ALL is False
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'https://mu-isystem.vercel.app',
    'https://node-mysql-signup-verification-api.onrender.com',
    'https://misbenedictocollege.netlify.app',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = Path(BASE_DIR / 'media')


# # Logging configuration
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': BASE_DIR / 'django.log',
#             'level': 'DEBUG',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'DangoDBApp': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }