import django_tables2 as tables
from django_tables2 import columns
from django_tables2.utils import A

from projects.models import Event


class MajorEventTable(tables.Table):
    title = columns.LinkColumn('event_detail', args=[A('pk')], attrs={
                               "td": {"class": "bold no-color"}})
    project = columns.Column(visible=True)
    type = columns.Column(visible=False)
    end_at = columns.DateColumn(format='d-M-y', visible=False)
    # timetable = columns.Column(visible=False)
    # partners = columns.Column(visible=False)
    # online = columns.Column(visible=False)
    # tickets = columns.Column(visible=False)
    # fees = columns.Column(visible=False)
    particip_num_predict = columns.Column(visible=False)
    particip_num_actual = columns.Column(visible=False)
    # link = columns.Column(visible=False)
    # registr_link = columns.Column(visible=False)
    # budget = columns.Column(visible=False)
    # contact_person = columns.Column(visible=False)
    # comment = columns.Column(visible=False)
    start_at = tables.DateTimeColumn(format='d-m-y')
    # end_at = tables.DateTimeColumn(format='d-m-y', visible=False)

    class Meta:
        model = Event
        fields = ('title', 'project', 'start_at', 'status')
