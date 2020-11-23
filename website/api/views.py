from django.contrib.auth import get_user_model
from rest_framework import viewsets

from projects.models import Event, Project
from .serializers import EventSerializer, ProjectSerializer
from projects.filters import EventFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
