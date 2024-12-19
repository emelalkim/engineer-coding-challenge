"""
Django settings for project.

Generated by 'django-admin startproject' using Django 3.2.
"""

from pathlib import Path
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Default value for the notification endpoint
NOTIFICATION_ENDPOINT = os.getenv("NOTIFICATION_ENDPOINT", "http://localhost:5001/notifications")

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'replace-this-with-a-secure-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'app',  # Custom app for user and legacy integration
]

MIDDLEWARE = []

ROOT_URLCONF = 'project.urls'

TEMPLATES = []

WSGI_APPLICATION = 'project.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_URL = '/static/'