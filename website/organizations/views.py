from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from projects.models import Event
from projects.filters import EventFilter
from .tables import MajorEventTable


class MajorTableView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     ExportMixin,
                     SingleTableMixin,
                     FilterView):
    model = Event
    permission_required = 'projects.view_event'
    table_class = MajorEventTable
    filterset_class = EventFilter
    template_name = 'major_event_table.html'
    paginate_by = 20
    dataset_kwargs = {'title': 'Events'}
    export_formats = ['csv', 'ods', 'xlsx']

    # exclude columns from table export:
    exclude_columns = ('actions')

    def get_queryset(self):
        return Event.objects.filter(supervisor__organization=self.request.user.organization)
