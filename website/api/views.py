from rest_framework import generics

from projects.models import Project
from .serializers import ProjectSerializer


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
