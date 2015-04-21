from common import *
import os

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['thimbleapp.herokuapp.com','staging-thimbleapp.herokuapp.com']

ADMINS = (
    ('Salil Gupta', 'salil.gupta323@gmail.com'),
    ('Henry Spindell','henryspindell2015@u.northwestern.edu'),
    ('Ryan Madden','ryanmadden2017@u.northwestern.edu')
)

MANAGERS = ADMINS

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

import dj_database_url
DATABASES['default'] = dj_database_url.config()


INSTALLED_APPS = INSTALLED_APPS + (
    'storages',
)

# static files (i.e. js, css ) served from AWS S3 Bucket
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
