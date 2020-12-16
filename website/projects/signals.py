from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from projects.models import Event, Project


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_example_event(sender, instance=None, created=False, **kwargs):
    if created:
        try:
            event = Event.objects.get(title='Example Event')
            event.make_clone(attrs={'title': f'Your {event.title}', 'status': 'd', 'supervisor': instance})
        except ObjectDoesNotExist:
            pass


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_example_project(sender, instance=None, created=False, **kwargs):
    if created:
        try:
            project = Project.objects.get(title='Example Project')
            project.make_clone(attrs={'title': f'Your {project.title}', 'status': 'd', 'supervisor': instance})
        except ObjectDoesNotExist:
            pass
