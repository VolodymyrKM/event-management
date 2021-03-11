from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from event_app.models import Event, EventType
from event_app.serializers import EventSerializer, EventTypeSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class EventTypeViewSet(ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [IsAuthenticated]
