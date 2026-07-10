
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CamerasViewSet, DogsEventViewSet, TrashEventViewSet, SuspiciousObjectEventViewSet,EventsViewSet,LogsViewSet,SettingsapiViewSet

router = DefaultRouter()
router.register(r'cameras', CamerasViewSet)
router.register(r'dogs',DogsEventViewSet)
router.register(r'trash',TrashEventViewSet)
router.register(r'suspicious_objects',SuspiciousObjectEventViewSet)
router.register(r'events',EventsViewSet)
router.register(r'logs',LogsViewSet)
router.register(r'settingsApi',SettingsapiViewSet)
urlpatterns = [
    path('', include(router.urls)),
]