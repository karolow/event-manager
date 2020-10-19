from django.views.generic import ListView

from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import (
    Project,
    Event,
)
from .tables import EventTable
from .filters import EventFilter


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'project_list.html'


class EventListView(ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'


class EventTableView(SingleTableView):
    model = Event
    table_class = EventTable
    template_name = 'event_table.html'


class FilteredEventTableView(SingleTableMixin, FilterView):
    model = Event
    table_class = EventTable
    template_name = "filtered_event_table.html"

    filterset_class = EventFilter
