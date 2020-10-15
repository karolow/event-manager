from django.db import models
from core.models import PersistentItem, Entry, ContactDetails


class Organizations(Entry, ContactDetails):
    pass


class Activities(PersistentItem):
    title = models.CharField(max_length=255)
