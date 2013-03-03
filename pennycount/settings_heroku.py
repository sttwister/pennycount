from settings import *

import dj_database_url
import os

DEFAULT_FROM_EMAIL = 'PennyCount <noreply@pennycount.com>'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
