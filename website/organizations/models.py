from django.db import models
from core.models import PersistentItem, Entry, ContactDetails


class Organization(Entry, ContactDetails):
    pass


class Activity(PersistentItem):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    number = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title
