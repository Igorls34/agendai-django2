from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-secret-key-change-me'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agendai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'agendai' / 'templates'],
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

WSGI_APPLICATION = 'agendai.wsgi.application'

ASGI_APPLICATION = 'agendai.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'pt-br'
LANGUAGES = [
    ('pt-br', _('Português (Brasil)')),
]

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'agendai' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # DESENVOLVIMENTO - imprime no console
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'YOUR_GMAIL_APP_PASSWORD'  # Substitua pela sua senha de app do Gmail

# Configurações do Twilio para WhatsApp
TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'  # Substitua pelo seu Account SID do Twilio
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'    # Substitua pelo seu Auth Token do Twilio
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Número do WhatsApp do Twilio (sandbox)

# Para SMS (mais fácil - funciona com qualquer número)
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'  # Seu número do Twilio

LOGIN_URL = '/admin/login/'  # Reuso do login admin para o dashboard leve
