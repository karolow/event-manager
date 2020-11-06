from django.contrib import admin
from .models import Type, Location

from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

admin.site.register(Type)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'street', 'city')
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
