"""
WSGI config for auction_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_backend.settings')

# Ensure startup exceptions are always visible in Railway logs, even before
# Django's own logging machinery is fully initialised.
logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

try:
    application = get_wsgi_application()
except Exception:
    logging.exception(
        "FATAL: Django WSGI application failed to initialise. "
        "The process will exit so Railway can surface the error."
    )
    sys.exit(1)
