from django import forms

from .models import Project, Event


class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'char_count', 'data-length': '100'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'data-length': '5000'}))

    class Meta:
        model = Project
        exclude = (
            'supervisor',
        )


class EventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'char_count', 'data-length': '100'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'data-length': '5000'}))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'data-length': '2000'}))

    class Meta:
        model = Event
        exclude = (
            'supervisor',
        )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('project_user')
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(supervisor=user)
