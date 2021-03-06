from rest_framework import viewsets

from events.models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.future.order_by('start')
    serializer_class = EventSerializer
