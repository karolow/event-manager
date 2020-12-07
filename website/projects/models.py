from django.db import models
from django.urls import reverse
from django.conf import settings

from model_clone import CloneMixin

from core.models import (
    Entry,
    Category,
    ContactDetails,
    Ownership,
    Status,
    Type,
    Location,
)
from organizations.models import Activity


class Project(Entry, ContactDetails):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    multiple_locations = models.TextField(max_length=1000, blank=True)

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

    class Meta:
        ordering = ['title']

    @property
    def place(self):
        if self.location:
            return self.location.name
        elif self.multiple_locations:
            return self.multiple_locations
        else:
            return ''


class Event(CloneMixin, Entry, Category, Ownership, Status):
    project = models.ForeignKey(
        Project,
        related_name='events',
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
    partners = models.TextField(max_length=1000, blank=True)
    online = models.BooleanField(default=False)
    tickets = models.BooleanField(default=False)
    fees = models.CharField(max_length=1000, blank=True)
    particip_num_predict = models.IntegerField(null=True, blank=True)
    particip_num_actual = models.IntegerField(null=True, blank=True)
    link = models.URLField(blank=True)
    registr_link = models.URLField(blank=True)
    budget = models.IntegerField(null=True, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    comment = models.TextField(max_length=2000, blank=True)

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])
