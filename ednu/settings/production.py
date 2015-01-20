from common import *
import os

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Salil Gupta', 'salil.gupta323@gmail.com'),
    ('Henry Spindell','henryspindell2015@u.northwestern.edu'),
    ('Ryan Madden','ryanmadden2017@u.northwestern.edu')
)

MANAGERS = ADMINS


import dj_database_url
DATABASES['default'] = dj_database_url.config()


INSTALLED_APPS = INSTALLED_APPS + (
#     'lockdown',
    'storages',
)


STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# MIDDLEWARE_CLASSES += ('lockdown.middleware.LockdownMiddleware', 'raygun_dot_io.middleware.RaygunDotIOMiddleware')
# LOCKDOWN_PASSWORDS = (os.environ['STAGE_PASSWORD'],)
# LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

STATIC_URL = 'http://%s.s3.amazonaws.com/' % os.environ['AWS_STATIC_FILES']