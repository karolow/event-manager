from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)

from django.db.models import Q

from projects.models import Event, Project
from projects.filters import EventFilter, ProjectFilter
from .tables import AllEventTable, AllProjectTable


class OrganizationEventTableView(LoginRequiredMixin,
                                 PermissionRequiredMixin,
                                 UserPassesTestMixin,
                                 ExportMixin,
                                 SingleTableMixin,
                                 FilterView):
    """
    Lists events of just one organization the user belongs to
    """

    model = Event
    permission_required = 'projects.view_event'
    table_class = AllEventTable
    filterset_class = EventFilter
    template_name = 'all_event_table.html'
    paginate_by = 20
    dataset_kwargs = {'title': 'Events'}
    export_formats = ['csv', 'ods', 'xlsx']

    # exclude columns from table export:
    exclude_columns = ('actions')

    def get_queryset(self):
        return Event.objects \
            .filter(supervisor__organization=self.request.user.organization) \
            .filter(~Q(status='d'))

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Coordinator', 'Custom']).exists() \
            or self.request.user.is_staff


class AllOrganizationsEventTableView(LoginRequiredMixin,
                                     PermissionRequiredMixin,
                                     UserPassesTestMixin,
                                     ExportMixin,
                                     SingleTableMixin,
                                     FilterView):

    """
    Lists events of all organizations
    """

    model = Event
    permission_required = 'projects.view_event'
    table_class = AllEventTable
    filterset_class = EventFilter
    template_name = 'all_event_table.html'
    paginate_by = 20
    dataset_kwargs = {'title': 'Events'}
    export_formats = ['csv', 'ods', 'xlsx']

    # exclude columns from table export:
    exclude_columns = ('actions')

    def get_queryset(self):
        return Event.objects.filter(~Q(status='d'))

    def test_func(self):
        return self.request.user.groups.filter(name='Follower').exists() \
            or self.request.user.is_staff


class OrganizationProjectTableView(LoginRequiredMixin,
                                   PermissionRequiredMixin,
                                   UserPassesTestMixin,
                                   ExportMixin,
                                   SingleTableMixin,
                                   FilterView):
    """
    Lists projects of just one organization the user belongs to
    """

    model = Project
    permission_required = 'projects.view_project'
    table_class = AllProjectTable
    filterset_class = ProjectFilter
    template_name = 'all_project_table.html'
    paginate_by = 20
    dataset_kwargs = {'title': 'Projects'}
    export_formats = ['csv', 'ods', 'xlsx']

    def get_queryset(self):
        return Project.objects \
            .filter(supervisor__organization=self.request.user.organization)

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Coordinator', 'Custom']).exists() \
            or self.request.user.is_staff


class AllOrganizationsProjectTableView(LoginRequiredMixin,
                                       PermissionRequiredMixin,
                                       UserPassesTestMixin,
                                       ExportMixin,
                                       SingleTableMixin,
                                       FilterView):

    """
    Lists projects of all organizations
    """

    model = Project
    permission_required = 'projects.view_project'
    table_class = AllProjectTable
    filterset_class = ProjectFilter
    template_name = 'all_project_table.html'
    paginate_by = 20
    dataset_kwargs = {'title': 'Projects'}
    export_formats = ['csv', 'ods', 'xlsx']

    def get_queryset(self):
        return Project.objects.all()

    def test_func(self):
        return self.request.user.groups.filter(name='Follower').exists() \
            or self.request.user.is_staff
