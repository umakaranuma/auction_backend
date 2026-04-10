"""
WSGI config for auction_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import logging
import os
import traceback

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_backend.settings')

logger = logging.getLogger(__name__)

_application = get_wsgi_application()


def application(environ, start_response):
    """Thin wrapper around the Django WSGI app that logs unhandled exceptions.

    Gunicorn swallows tracebacks in some configurations, so any exception that
    escapes Django's own error handling is caught here, written to stderr via
    the standard logging machinery, and then re-raised so the worker still
    returns a 500 to the client.
    """
    try:
        return _application(environ, start_response)
    except Exception:
        logger.exception(
            "Unhandled exception in WSGI application\n%s", traceback.format_exc()
        )
        raise
