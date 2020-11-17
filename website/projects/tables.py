import django_tables2 as tables
from django_tables2 import columns
from django_tables2.utils import A

from .models import Event, Project


class EventTable(tables.Table):
    ACTIONS = '''
       <span><a href="{% url 'event_update' record.id %}"><i class="material-icons">edit</i></a>
       <span><a href="{% url 'event_duplicate' record.id %}"><i class="material-icons">content_copy</i></a>
       <a href="{% url 'event_delete' record.id %}"><i class="material-icons">delete</i></a></span>
    '''

    title = columns.LinkColumn('event_detail', args=[A('pk')])
    project = columns.Column()
    type = columns.Column(visible=False)
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
    end_at = tables.DateTimeColumn(format='d-m-y')
    actions = tables.TemplateColumn(ACTIONS, verbose_name="")

    class Meta:
        model = Event
        fields = ('title', 'project', 'start_at', 'end_at', 'status', 'actions')


class ProjectTable(tables.Table):
    ACTIONS = '''
       <span><a href="{% url 'project_update' record.id %}"><i class="material-icons">edit</i></a>
       <a href="{% url 'project_delete' record.id %}"><i class="material-icons">delete</i></a></span>
    '''

    title = columns.LinkColumn('project_detail', args=[A('pk')])
    actions = tables.TemplateColumn(ACTIONS, verbose_name="")

    class Meta:
        model = Project
        fields = ('title', 'actions')
