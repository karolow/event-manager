from django.contrib.auth.models import AbstractUser
from django.db import models

from organizations.models import Organization


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=255, blank=True)
