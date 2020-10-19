import django_tables2 as tables
from .models import Event


class EventTable(tables.Table):
    class Meta:
        model = Event
        template_name = "django_tables2/bootstrap.html"
        fields = ("title", "location", "status")
