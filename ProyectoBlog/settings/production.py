from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django-generis-blog.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3kmclk843v4k8',
        'USER':'pukdrsdgrzhyps',
        'PASSWORD':'2e829bd0a24524633a3803c2db4b9935f15af1afd55aeb4a4e19f3707d879dd3',
        'HOST':'ec2-54-209-221-231.compute-1.amazonaws.com',
        'PORT':5432,
    }
}