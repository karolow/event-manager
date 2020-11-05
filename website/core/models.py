import uuid
from django.db import models
from multiselectfield import MultiSelectField


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


class Entry(PersistentItem):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000, blank=True)
    location = models.CharField(max_length=255, blank=True)
    room = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class ContactDetails(models.Model):
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class Ownership(models.Model):
    OWN = 'o'
    COLLABORATION = 'c'
    EXTERNAL = 'e'

    OWNERSHIP_CHOICES = [
        (OWN, 'Own'),
        (COLLABORATION, 'Collaboration'),
        (EXTERNAL, 'External'),
    ]

    ownership = models.CharField(
        max_length=1,
        choices=OWNERSHIP_CHOICES,
        default=OWN,
    )

    class Meta:
        abstract = True


class Status(models.Model):
    PUBLISHED = 'p'
    DRAFT = 'd'
    CANCELLED = 'c'

    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (CANCELLED, 'Cancelled'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PUBLISHED,
    )

    class Meta:
        abstract = True


class Type(PersistentItem):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    FIELDS = (
        ('architecture', 'architecture'),
        ('heritage', 'heritage'),
        ('cultural education', 'cultural education'),
        ('cinema', 'cinema'),
        ('photography', 'photography'),
        ('video games', 'video games'),
        ('interdisciplinary', 'interdisciplinary'),
        ('cabaret', 'cabaret'),
        ('cuisine', 'cuisine'),
        ('literature', 'literature'),
        ('fashion', 'fashion'),
        ('music', 'music'),
        ('new media', 'new media'),
        ('traveling', 'traveling'),
        ('design', 'desing'),
        ('urban intervension', 'urban intervension'),
        ('craft', 'craft'),
        ('street art', 'street art'),
        ('visual arts', 'visual arts'),
        ('dance', 'dance'),
        ('theatre', 'theatre'),
        ('other', 'other'),
    )

    fields = MultiSelectField(choices=FIELDS, null=True, blank=True)

    AUDIENCES = (
        ('young kids', 'young kids'),
        ('primary school', 'primary school'),
        ('teenagers', 'teenagers'),
        ('students', 'students'),
        ('adults', 'adults'),
        ('seniors', 'seniors'),
        ('all', 'all')
    )

    audiences = MultiSelectField(choices=AUDIENCES, null=True, blank=True)

    class Meta:
        abstract = True
