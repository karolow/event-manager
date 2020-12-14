from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q

from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.detail import SingleObjectMixin

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.contrib.auth.decorators import login_required, permission_required

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
                       PermissionRequiredMixin,
                       ExportMixin,
                       SingleTableMixin,
                       FilterView):
    model = Project
    permission_required = 'projects.view_project'
    table_class = ProjectTable
    filterset_class = ProjectFilter
    template_name = 'project_table.html'
    paginate_by = 5
    dataset_kwargs = {'title': 'Projects'}
    export_formats = ['csv', 'ods', 'xlsx']

    # exclude columns from table export:
    exclude_columns = ('activity')

    def get_queryset(self):
        return Project.objects.filter(supervisor=self.request.user)


class ProjectCreateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        CreateView):
    form_class = ProjectForm
    permission_required = 'projects.add_project'
    success_url = reverse_lazy('project_table')
    template_name = 'project.html'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.supervisor = self.request.user
        project.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs.update({'project_user': self.request.user})
        return kwargs


class ProjectDetailView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        SingleObjectMixin,
                        ListView):
    permission_required = 'projects.view_project'
    paginate_by = 1
    template_name = 'project_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(
            queryset=Project.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object
        return context

    def get_queryset(self):
        return self.object.events.filter(~Q(status='d')).order_by('-start_at')


class ProjectUpdateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        UserPassesTestMixin,
                        UpdateView):
    model = Project
    permission_required = 'projects.change_project'
    form_class = ProjectForm
    success_url = reverse_lazy('project_table')
    template_name = 'project.html'

    def get_form_kwargs(self):
        kwargs = super(ProjectUpdateView, self).get_form_kwargs()
        kwargs.update({'project_user': self.request.user})
        return kwargs

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


@login_required
@permission_required('projects.add_project', raise_exception=True)
def duplicate_project(request, **kwargs):
    """
    Create a duplicate of project
    """
    project = Project.objects.get(pk=kwargs.get('pk'))
    new_project = project.make_clone(attrs={'title': f'COPY OF {project.title}', 'status': 'd'})
    return redirect('project_update', pk=new_project.pk)


class ProjectDeleteView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        UserPassesTestMixin,
                        DeleteView):

    model = Project
    permission_required = 'projects.delete_project'
    success_url = reverse_lazy('project_table')
    template_name = 'project_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


class EventTableView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     ExportMixin,
                     SingleTableMixin,
                     FilterView):
    model = Event
    permission_required = 'projects.view_event'
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
                      PermissionRequiredMixin,
                      CreateView):
    form_class = EventForm
    permission_required = 'projects.add_event'
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
                      PermissionRequiredMixin,
                      # UserPassesTestMixin,
                      DetailView):
    model = Event
    permission_required = 'projects.view_event'
    context_object_name = 'event'
    template_name = 'event_detail.html'

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.supervisor.organization == self.request.user.organization


class EventUpdateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      UserPassesTestMixin,
                      UpdateView):
    model = Event
    permission_required = 'projects.change_event'
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


@login_required
@permission_required('projects.add_event', raise_exception=True)
def duplicate_event(request, **kwargs):
    """
    Create a duplicate of event
    """
    event = Event.objects.get(pk=kwargs.get('pk'))
    new_event = event.make_clone(attrs={'title': f'COPY OF {event.title}', 'status': 'd'})
    return redirect('event_update', pk=new_event.pk)


class EventDeleteView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      UserPassesTestMixin,
                      DeleteView):
    model = Event
    permission_required = 'projects.delete_event'
    success_url = reverse_lazy('event_table')
    template_name = 'event_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.supervisor == self.request.user


class LocationCreateView(LoginRequiredMixin,
                         PermissionRequiredMixin,
                         CreateView):
    model = Location
    permission_required = 'core.add_location'
    form_class = LocationForm
    success_url = reverse_lazy('event_table')
    template_name = 'location_modal.html'


class TextEventInfoView(SingleObjectMixin, View):
    model = Event

    def get(self, request, *args, **kwargs):
        event = self.get_object()

        start = event.start_at.strftime('%d-%m-%Y %H:%M')
        end = event.end_at.strftime('–%H:%M') if event.start_at.strftime(
            '%d-%m-%Y') == event.end_at.strftime('%d-%m-%Y') else event.end_at.strftime(' | %d-%m-%Y %H:%M')
        type = f'{event.type}' if not event.online else f'{event.type} online'
        location = f'{event.location}' if not event.room else f'{event.location}, {event.room}'

        content = [
            event.title,
            type,
            f'{start}{end}',
            location,
            event.description,
            event.link,
        ]
        content_export = '\n\n'.join(content)
        return HttpResponse(content_export, content_type='text/plain; charset=utf8')
