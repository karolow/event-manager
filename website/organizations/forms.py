from django import forms

from .models import Event


class MajorEventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = (
            'supervisor',
        )
