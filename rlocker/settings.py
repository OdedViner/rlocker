"""
Django settings for rlocker project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import yaml
import rlocker.utils as u

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Could add here for debugging only: os.environ['DJANGO_SECRET'] = $YOUR_SECRET
SECRET_KEY = os.environ.get("DJANGO_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
# We use string by purpose since its env var
DEBUG = os.environ.get("DEBUG") == "True"

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "patch_notifier.apps.PatchNotifierConfig",
    "admin_tools.apps.AdminToolsConfig",
    "health.apps.HealthConfig",
    "dashboard.apps.DashboardConfig",
    "rqueue.apps.RqueueConfig",
    "api.apps.ApiConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "lockable_resource.apps.LockableResourceConfig",
    "account.apps.AccountConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "resoucesdc",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "patch_notifier.middleware.CheckFirstVisitMiddleware",
]

ROOT_URLCONF = "rlocker.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "rqueue.context_processors.rqueue_context_processors",
                "rlocker.context_processors.global_context_processors",
            ],
        },
    },
]

WSGI_APPLICATION = "rlocker.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

PROD_DB = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRESQL_DATABASE"),
        "USER": os.environ.get("POSTGRESQL_USER"),
        "PASSWORD": os.environ.get("POSTGRESQL_PASSWORD"),
        "HOST": os.environ.get("DATABASE_SERVICE_NAME"),
    }
}

DEV_DB = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


DATABASES = PROD_DB if not os.environ.get("USE_DEV_DB") == "True" else DEV_DB

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# Location of the static files for debug mode, the location that the Django should search for:
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# Location where the static files would be collected once running python manage.py collectstatic --noinput
STATIC_ROOT = BASE_DIR / "nginx" / "static"

# Addons support
USE_DEV_ADDONS = True if os.environ.get("USE_DEV_ADDONS") == "True" else False
ADDONS_FILE = BASE_DIR / "addons_dev.txt" if USE_DEV_ADDONS else BASE_DIR / "addons.txt"


INSTALLED_ADDONS = []
try:
    with open(ADDONS_FILE, "r") as f:
        INSTALLED_ADDONS = u.CustomList(f.readlines(), no_duplicates=True)
        # WA: DO NOT include new lines in the list if they exist
        INSTALLED_ADDONS.remove_if_exist("\n")
except FileNotFoundError as e:
    print(
        f"File not found {ADDONS_FILE} \n"
        "Perhaps you need to execute python manage.py prepare_installed_addons ?"
    )
finally:
    # Extend the INSTALLED_APPS based on the installed addons (whether if from dev addons or not)
    INSTALLED_APPS.extend(INSTALLED_ADDONS)
