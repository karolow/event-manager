import uuid
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.gis.db import models
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
        (OWN, _('Own')),
        (COLLABORATION, _('Collaboration')),
        (EXTERNAL, _('External')),
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
        (PUBLISHED, _('Published')),
        (DRAFT, _('Draft')),
        (CANCELLED, _('Cancelled')),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PUBLISHED,
    )

    class Meta:
        abstract = True


class Type(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Category(models.Model):
    FIELDS = (
        ('architecture', _('architecture')),
        ('heritage', _('heritage')),
        ('cultural education', _('cultural education')),
        ('ecology', _('ecology')),
        ('cinema', _('cinema')),
        ('photography', _('photography')),
        ('video games', _('video games')),
        ('interdisciplinary', _('interdisciplinary')),
        ('cabaret', _('cabaret')),
        ('cuisine', _('cuisine')),
        ('folk/local culture', _('folk/local culture')),
        ('literature', _('literature')),
        ('fashion', _('fashion')),
        ('music', _('music')),
        ('science', _('science')),
        ('new media', _('new media')),
        ('traveling', _('traveling')),
        ('design', _('desing')),
        ('urban intervension', _('urban intervension')),
        ('craft', _('craft')),
        ('street art', _('street art')),
        ('visual arts', _('visual arts')),
        ('dance', _('dance')),
        ('theatre', _('theatre')),
        ('other', _('other')),
    )

    fields = MultiSelectField(choices=FIELDS, null=True, blank=True)

    AUDIENCES = (
        ('young kids', _('young kids')),
        ('primary school', _('primary school')),
        ('teenagers', _('teenagers')),
        ('students', _('students')),
        ('adults', _('adults')),
        ('seniors', _('seniors')),
        ('all', _('all'))
    )

    audiences = MultiSelectField(choices=AUDIENCES, null=True, blank=True)

    AUDIENCE_GROUPS = (
        ('disadvantaged groups', _('disadvantaged groups')),
        ('people with disabilities', _('people with disabilities')),
        ('district residents', _('district residents')),
        ('pupils', _('pupils')),
        ('artists / creators', _('artists / creators')),
        ('event organizers', _('event organizers')),
        ('ngo representatives', _('ngo representatives')),
        ('educators', _('educators')),
        ('activists', _('activists')),
    )

    audience_groups = MultiSelectField(choices=AUDIENCE_GROUPS, null=True, blank=True)

    MUNICIPAL_PROGRAMS = (
        ('Akacja Lato w mieście', _('Akacja Lato w mieście')),
        ('Akcja Zima w mieście', _('Akcja Zima w mieście')),
        ('Dla seniorów', _('Dla seniorów')),
        ('Katowice bez barier', _('Katowice bez barier')),
        ('Wydarzenie okolicznościowe', _('Wydarzenie okolicznościowe')),
    )

    municipal_programs = MultiSelectField(choices=MUNICIPAL_PROGRAMS, null=True, blank=True)

    class Meta:
        abstract = True


class Location(PersistentItem):
    name = models.CharField(max_length=50)
    coordinates = models.PointField()
    street = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.name
