from django import forms

from .models import Project, Event


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = (
            'supervisor',
        )


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = (
            'supervisor',
        )
