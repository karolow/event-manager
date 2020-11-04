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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('project_user')
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(supervisor=user)
