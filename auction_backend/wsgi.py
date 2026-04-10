"""
WSGI config for auction_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.
Vercel's Python runtime also expects ``app`` (see Vercel Python docs).

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auction_backend.settings")

application = get_wsgi_application()
app = application
