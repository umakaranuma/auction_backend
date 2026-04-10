"""
WSGI config for auction_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import traceback

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_backend.settings')


class ExceptionLoggingMiddleware:
    """WSGI middleware that catches all request-level exceptions, logs them
    with full tracebacks to stderr, and re-raises so gunicorn still returns
    a 500 to the client."""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        method = environ.get('REQUEST_METHOD', 'UNKNOWN')
        path = environ.get('PATH_INFO', '/')
        try:
            return self.app(environ, start_response)
        except Exception:
            print(
                f"UNHANDLED EXCEPTION during {method} {path}\n"
                + traceback.format_exc(),
                file=sys.stderr,
                flush=True,
            )
            raise


application = ExceptionLoggingMiddleware(get_wsgi_application())
