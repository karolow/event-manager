from django.views.generic import ListView

from .models import Project, Event


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'


class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'
