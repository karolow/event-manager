import django_tables2 as tables
from django_tables2 import columns
from django_tables2.utils import A

from .models import Event


class EventTable(tables.Table):
    ACTIONS = '''
       <span><a href="{% url 'event_update' record.id %}"><i class="material-icons">edit</i></a>
       <span><a href="{% url 'event_duplicate' record.id %}"><i class="material-icons">content_copy</i></a>
       <a href="{% url 'event_delete' record.id %}"><i class="material-icons">delete</i></a></span>
    '''

    title = columns.LinkColumn('event_detail', args=[A('pk')])
    project = columns.Column(visible=False)
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
    actions = tables.TemplateColumn(ACTIONS, verbose_name="")

    class Meta:
        model = Event
        fields = ('title', 'start_at', 'status', 'actions')
