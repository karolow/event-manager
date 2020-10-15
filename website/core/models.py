import uuid
from django.db import models


class PersistentItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000, blank=True)
    location = models.CharField(max_length=255)
    room = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class ContactDetails(models.Model):
    website = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True
