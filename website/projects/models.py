from django.db import models
from django.conf import settings
from core.models import (
    Entry,
    Categories,
    ContactDetails,
    Ownership,
    Status,
    Type,
)
from organizations.models import Activity


class Project(Entry, ContactDetails):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.SET_NULL,
        null=True
    )
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )


class Event(Entry, Categories, Ownership, Status):
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
    )
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    timetable = models.TextField(max_length=2000, blank=True)
    partners = models.CharField(max_length=1000, blank=True)
    online = models.BooleanField(default=False)
    tickets = models.BooleanField(default=False)
    fees = models.CharField(max_length=1000, blank=True)
    particip_num_predict = models.IntegerField(null=True, blank=True)
    particip_num_actual = models.IntegerField(null=True, blank=True)
    link = models.URLField(blank=True)
    registr_link = models.URLField(blank=True)
    budget = models.IntegerField(null=True, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    comment = models.CharField(max_length=2000, blank=True)
