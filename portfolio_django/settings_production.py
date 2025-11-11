"""
Production settings for portfolio_django project.
"""

import os
import secrets
import string
from pathlib import Path
from .settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Generate a secret key if not provided (for development/testing only)
# In production, always set DJANGO_SECRET_KEY environment variable in Render!
if not SECRET_KEY:
    # Generate a random secret key
    chars = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    SECRET_KEY = ''.join(secrets.choice(chars) for _ in range(50))
    import warnings
    warnings.warn(
        "SECRET_KEY not set in environment! Generated a temporary key. "
        "Set DJANGO_SECRET_KEY environment variable in Render dashboard for production!",
        UserWarning
    )

# SECURITY WARNING: update this list with your domain names
# Base allowed hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'personal-portfolio-django-8i5w.onrender.com',  # Your Render domain
]

# Add hosts from environment variable (comma-separated)
# This allows you to set ALLOWED_HOSTS in Render's environment variables
if os.environ.get('ALLOWED_HOSTS'):
    ALLOWED_HOSTS.extend([host.strip() for host in os.environ.get('ALLOWED_HOSTS').split(',')])

# Security Settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Use PostgreSQL if credentials are provided, otherwise fallback to SQLite
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')

if DB_PASSWORD and DB_HOST:
    # Use PostgreSQL if credentials are available
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'portfolio_db'),
            'USER': os.environ.get('DB_USER', 'portfolio_user'),
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }
else:
    # Fallback to SQLite for free tier or when PostgreSQL isn't configured
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    import warnings
    warnings.warn(
        "PostgreSQL credentials not found. Using SQLite database. "
        "For production, set up a PostgreSQL database in Render and configure DB_* environment variables.",
        UserWarning
    )

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CORS settings for production
CORS_ALLOWED_ORIGINS = [
    "https://personal-portfolio-django-8i5w.onrender.com",
]

# Add CORS origins from environment variable (comma-separated)
if os.environ.get('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS.extend([origin.strip() for origin in os.environ.get('CORS_ALLOWED_ORIGINS').split(',')])

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_USER')

# Twilio SMS Configuration
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
RECIPIENT_PHONE_NUMBER = os.environ.get('YOUR_PHONE_NUMBER')

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'core': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Cache Configuration
# Use Redis if available, otherwise fallback to in-memory cache
REDIS_URL = os.environ.get('REDIS_URL')
if REDIS_URL and REDIS_URL.startswith('redis://'):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': REDIS_URL,
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = 'default'
else:
    # Fallback to in-memory cache if Redis isn't available
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }
    # Use database sessions if Redis cache isn't available
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'
    import warnings
    warnings.warn(
        "Redis URL not found. Using in-memory cache and database sessions. "
        "For production, set up Redis in Render and configure REDIS_URL environment variable.",
        UserWarning
    )

# Rate Limiting
# Only enable if cache is properly configured (Redis)
RATELIMIT_ENABLE = bool(REDIS_URL and REDIS_URL.startswith('redis://'))
RATELIMIT_USE_CACHE = 'default'

# File Upload Security
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755

# Allowed file types for uploads
ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
ALLOWED_DOCUMENT_TYPES = ['application/pdf', 'application/msword', 
                          'application/vnd.openxmlformats-officedocument.wordprocessingml.document']

# Maximum file sizes
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB
MAX_DOCUMENT_SIZE = 10 * 1024 * 1024  # 10MB

