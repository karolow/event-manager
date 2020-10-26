from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin

from .models import (
    Project,
    Event,
)
from .forms import (
    ProjectForm,
    EventForm,
)
from .tables import EventTable
from .filters import EventFilter


# to do – change ListView to TableView
class ProjectTableView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'project_table.html'


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
                        DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project_detail.html'


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
