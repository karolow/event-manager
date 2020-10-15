from django.contrib.auth.models import AbstractUser
from django.db import models

from organizations.models import Organizations


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        Organizations,
        on_delete=models.SET_NULL,
        null=True
    )
    phone = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=255, blank=True)
