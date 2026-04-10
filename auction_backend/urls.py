from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.db import connection
from django.utils import timezone


def health(request):
    return JsonResponse({"status": "ok"})


def health_check(request):
    db_status = "disconnected"
    overall_status = "error"
    message = "Database connection failed"

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        db_status = "connected"
        overall_status = "ok"
        message = "Application is running and database is connected"
    except Exception as exc:
        message = f"Database connection failed: {exc}"

    http_status = 200 if overall_status == "ok" else 503
    return JsonResponse(
        {
            "status": overall_status,
            "database": db_status,
            "message": message,
            "timestamp": timezone.now().isoformat(),
        },
        status=http_status,
    )

urlpatterns = [
    path('', health),
    path('health/', health_check),
    path('admin/', admin.site.urls),
    path('api/', include('players.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
