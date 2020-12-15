import django_tables2 as tables
from django_tables2 import columns
from django_tables2.utils import A

from .models import Event, Project


class EventTable(tables.Table):
    ACTIONS = '''
       <span style="white-space: nowrap">
           <a href="{% url 'event_update' record.id %}"><i class="table-icon material-icons icon-blue">edit</i></a>
           <a href="{% url 'event_duplicate' record.id %}"><i class="table-icon material-icons icon-blue">content_copy</i></a>
           <a href="{% url 'event_delete' record.id %}"><i class="table-icon material-icons icon-red">delete</i></a>
       </span>
    '''

    title = columns.LinkColumn('event_detail', args=[A('pk')], attrs={
                               "td": {"class": "bold no-color"}})
    project = columns.Column(visible=True,
                             attrs={"th": {"class": "hide-on-small-only"},
                                    "td": {"class": "hide-on-small-only"}})
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
    start_at = tables.DateTimeColumn(format='d-m-y', visible=True,
                                     attrs={"th": {"class": "hide-on-med-and-down"},
                                            "td": {"class": "hide-on-med-and-down"}})
    end_at = tables.DateTimeColumn(format='d-m-y', visible=True,
                                   attrs={"th": {"class": "hide-on-med-and-down"},
                                          "td": {"class": "hide-on-med-and-down"}})
    status = tables.Column(visible=True,
                           attrs={"th": {"class": "hide-on-med-and-down"},
                                  "td": {"class": "hide-on-med-and-down"}})
    actions = tables.TemplateColumn(ACTIONS, verbose_name="",
                                    attrs={"td": {"class": "text-align: right"}})

    class Meta:
        model = Event
        fields = ('title', 'project', 'start_at', 'end_at', 'status', 'actions')


class ProjectTable(tables.Table):
    ACTIONS = '''
       <span style="white-space: nowrap">
           <a href="{% url 'project_update' record.id %}"><i class="table-icon material-icons icon-blue">edit</i></a>
           <a href="{% url 'project_delete' record.id %}"><i class="table-icon material-icons icon-red">delete</i></a>
       </span>
    '''

    title = columns.LinkColumn('project_detail', args=[A('pk')], attrs={
        "td": {"class": "bold no-color"}})
    activity = columns.Column(verbose_name='Platform', visible=True,
                              attrs={"th": {"class": "hide-on-small-only"},
                                     "td": {"class": "hide-on-small-only"}})
    contact_person = columns.Column(visible=True,
                                    attrs={"th": {"class": "hide-on-small-only"},
                                           "td": {"class": "hide-on-small-only"}})
    website = columns.Column(visible=False)
    email = columns.Column(visible=True,
                           attrs={"th": {"class": "hide-on-med-and-down"},
                                  "td": {"class": "hide-on-med-and-down"}})
    actions = tables.TemplateColumn(ACTIONS, verbose_name="",
                                    attrs={"td": {"class": "text-align: right"}})

    class Meta:
        model = Project
        fields = ('title', 'activity', 'contact_person', 'email', 'website', 'actions')
