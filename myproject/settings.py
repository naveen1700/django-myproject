"""
Django settings for myproject project (Production-ready for Render).
"""

import os
from pathlib import Path

import dj_database_url
import pymysql
pymysql.install_as_MySQLdb()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Security & Environment
# -----------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')  # Use env var in production

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allowed Hosts
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,django-myproject-2.onrender.com"
).split(",")

# CSRF Trusted Origins (update with your Render URL)
CSRF_TRUSTED_ORIGINS = [
    "https://django-myproject-2.onrender.com",
    "https://www.django-myproject-2.onrender.com",
]

# -----------------------------
# Applications
# -----------------------------
INSTALLED_APPS = [
    'naveen',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# -----------------------------
# Database
# -----------------------------
# Use PostgreSQL in Render (DATABASE_URL is provided by Render automatically)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv(
            'DATABASE_URL',
            'postgresql://postgres:postgres@localhost:5432/myproject_db'
        ),
        conn_max_age=600,
    )
}

# -----------------------------
# Password Validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# Static Files
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# -----------------------------
# Default Primary Key
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
