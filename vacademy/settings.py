import os
import socket
from os.path import abspath, dirname, join
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_DIR = BASE_DIR.parent


def root(*dirs):
    base_dir = join(dirname(__file__), "..", "..")
    return abspath(join(base_dir, *dirs))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_TOOLBAR = os.environ.get("DEBUG_TOOLBAR", default=False)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local
    "apps.core",
    "apps.blog",
    "apps.akhdar",
    "apps.lne",
    "apps.home",
    "apps.masterclass",
    # third party
    "widget_tweaks",
    "rest_framework",
    "phonenumber_field",
]

if DEBUG and DEBUG_TOOLBAR:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]
else:
    MIDDLEWARE = []


MIDDLEWARE += [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vacademy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # local
                "apps.core.mixins.context_processors.copy_rights",
            ],
        },
    },
]

WSGI_APPLICATION = "vacademy.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 12},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "apps.core.validators.NumberValidator", "OPTIONS": {"min_digits": 3}},
    {"NAME": "apps.core.validators.password_validator.UppercaseValidator"},
    {"NAME": "apps.core.validators.password_validator.LowercaseValidator"},
    {"NAME": "apps.core.validators.password_validator.SymbolValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

BASE_STATIC_FILE = BASE_DIR / "static",
MASTERCLASS_STATIC_FILE = BASE_DIR / 'apps/masterclass/static'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / 'apps/masterclass/static'
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# MEDIA_ROOT = root("media")
# STATIC_ROOT = root("static_root")
# STATICFILES_DIRS = [root("static")]
# media
MEDIA_URL = "/media/"
MEDIA_DIR = ROOT_DIR / "media"
MEDIA_ROOT = MEDIA_DIR

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] [{asctime}] in [{pathname}/{funcName}:#{lineno}] [{message}]",
            "style": "{",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "[{levelname}] {message}", "style": "{",},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "root": {"handlers": ["console"], "level": "DEBUG",},
}

QUIZ_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

ACCOUNT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": "",
}
INTERNAL_IPS = [
    "127.0.0.1",
    socket.gethostbyname(socket.gethostname())[:-1] + "1",  # machine ip
]

# Custom debug toolbar panels
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]


EGYPT_CODE_PREFIX = 20

LOGIN_REDIRECT_URL = 'home:all'
# LOGOUT_REDIRECT_URL = "home:login"


# ############ react app ##############

# FRONTEND_ROOT = BASE_DIR / 'frontend/build'

# print(FRONTEND_ROOT)
