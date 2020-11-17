from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin

from .models import (
    Project,
    Event,
)
from core.models import Location

from .forms import (
    ProjectForm,
    EventForm,
    LocationForm,
)
from .tables import EventTable, ProjectTable
from .filters import EventFilter, ProjectFilter


class ProjectTableView(LoginRequiredMixin,
                       ExportMixin,
                       SingleTableMixin,
                       FilterView):
    model = Project
    table_class = ProjectTable
    filterset_class = ProjectFilter
    template_name = 'project_table.html'
    paginate_by = 2
    dataset_kwargs = {'title': 'Projects'}
    export_formats = ['csv', 'ods', 'xlsx']

    # exclude columns from table export:
    exclude_columns = ('activity')

    def get_queryset(self):
        return Project.objects.filter(supervisor=self.request.user)


class ProjectCreateView(LoginRequiredMixin,
                        CreateView):
    form_class = ProjectForm
    success_url = reverse_lazy('project_table')
    template_name = 'project.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.supervisor = self.request.user
        project.save()
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin,
                        SingleObjectMixin,
                        ListView):
    paginate_by = 5
    template_name = 'project_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Project.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object
        return context

    def get_queryset(self):
        user = self.request.user
        return self.object.event_set.all().filter(supervisor=user)


class ProjectUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_table')
    template_name = 'project.html'

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


def duplicate_project(request, **kwargs):
    """
    Create a duplicate of project
    """
    project = Project.objects.get(pk=kwargs.get('pk'))
    new_project = project.make_clone(attrs={'title': f'COPY OF {project.title}', 'status': 'd'})
    return redirect('project_update', pk=new_project.pk)


class ProjectDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        DeleteView):

    model = Project
    success_url = reverse_lazy('project_table')
    template_name = 'project_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


class EventTableView(LoginRequiredMixin,
                     ExportMixin,
                     SingleTableMixin,
                     FilterView):
    model = Event
    table_class = EventTable
    filterset_class = EventFilter
    template_name = 'event_table.html'
    paginate_by = 10
    dataset_kwargs = {'title': 'Events'}
    export_formats = ['csv', 'ods', 'xlsx']

    # exclude columns from table export:
    exclude_columns = ('actions')

    def get_queryset(self):
        return Event.objects.filter(supervisor=self.request.user)


class EventCreateView(LoginRequiredMixin,
                      CreateView):
    form_class = EventForm
    success_url = reverse_lazy('event_table')
    template_name = 'event.html'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.supervisor = self.request.user
        event.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(EventCreateView, self).get_form_kwargs()
        kwargs.update({'project_user': self.request.user})
        return kwargs


class EventDetailView(LoginRequiredMixin,
                      DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event_detail.html'


class EventUpdateView(LoginRequiredMixin,
                      UserPassesTestMixin,
                      UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event_table')
    template_name = 'event.html'

    def get_form_kwargs(self):
        kwargs = super(EventUpdateView, self).get_form_kwargs()
        kwargs.update({'project_user': self.request.user})
        return kwargs

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


def duplicate_event(request, **kwargs):
    """
    Create a duplicate of event
    """
    event = Event.objects.get(pk=kwargs.get('pk'))
    new_event = event.make_clone(attrs={'title': f'COPY OF {event.title}', 'status': 'd'})
    return redirect('event_update', pk=new_event.pk)


class EventDeleteView(LoginRequiredMixin,
                      UserPassesTestMixin,
                      DeleteView):
    model = Event
    success_url = reverse_lazy('event_table')
    template_name = 'event_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


class LocationCreateView(LoginRequiredMixin,
                         CreateView):
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('event_table')
    template_name = 'location_modal.html'
