import logging
from django.urls import path, include
from rest_framework.routers import DefaultRouter

logger = logging.getLogger(__name__)

router = DefaultRouter()

try:
    from .views import TournamentViewSet, TeamViewSet, PlayerViewSet

    router.register(r'tournaments', TournamentViewSet)
    router.register(r'teams', TeamViewSet)
    router.register(r'players', PlayerViewSet)

    logger.info("[players.urls] ViewSets registered successfully.")
except Exception as e:
    logger.exception(
        "[players.urls] Failed to import or register ViewSets — "
        "API routes will be unavailable. Error: %s", e
    )

urlpatterns = [
    path('', include(router.urls)),
]
