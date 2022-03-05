import os
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []


hostname = os.environ['DBHOST']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'] + "@" + hostname,
        'PASSWORD': os.environ['DBPASS'] 
    }
}


if 'WEBSITE_HOSTNAME' in os.environ: # Running on Azure
    from .azure import *