"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys, site

from django.core.wsgi import get_wsgi_application

site.addsitedir("/home/myvenv/envs/webapp/lib/python3.6/site-packages")
sys.path.append("/home/myvenv/envs//")
sys.path.append("/home/myvenv/envs/mysite")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
