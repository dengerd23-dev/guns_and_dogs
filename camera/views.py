from rest_framework import viewsets
from .models import Cameras, DogEvents, TrashEvent, SuspiciousObjectEvent, Events, Logs, Settings_API
from .serializers import CamerasSerializer, DogsEventsSerializer, TrashEventsSerializer, \
    SuspiciousObjectEventSerializer, EventsSerializer,Settings_APISerializer,LogsSerializer


# Create your views here.
class CamerasViewSet(viewsets.ModelViewSet):
    queryset = Cameras.objects.all()
    serializer_class = CamerasSerializer

class DogsEventViewSet(viewsets.ModelViewSet):
    queryset = DogEvents.objects.all()
    serializer_class = DogsEventsSerializer

class TrashEventViewSet(viewsets.ModelViewSet):
    queryset = TrashEvent.objects.all()
    serializer_class = TrashEventsSerializer

class SuspiciousObjectEventViewSet(viewsets.ModelViewSet):
    queryset = SuspiciousObjectEvent.objects.all()
    serializer_class = SuspiciousObjectEventSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer

class SettingsapiViewSet(viewsets.ModelViewSet):
    queryset = Settings_API.objects.all()
    serializer_class = Settings_APISerializer


