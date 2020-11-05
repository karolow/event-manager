from django.contrib.auth.models import AbstractUser
from django.db import models

from organizations.models import Organization


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=255, blank=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
