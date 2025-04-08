"""
WSGI config for chris_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys
sys.path.insert(0, '/home/chrys/Documents/projects/chris_potfolio/chris_portfolio')

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chris_portfolio.settings')

application = get_wsgi_application()
