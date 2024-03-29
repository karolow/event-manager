from django import forms
from django.utils.translation import ugettext_lazy as _

from mapwidgets.widgets import GooglePointFieldWidget

from .models import Project, Event
from core.models import Location
from organizations.models import Activity


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
        help_texts = {
            'multiple_locations': _('Use for multiple locations, e.g. Katowice, Bytom'),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('project_user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['activity'].queryset = Activity.objects.filter(
            organization=user.organization)


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
        request = kwargs.pop('request')
        user = request.user
        project_pk = request.GET.get('next')
        super(EventForm, self).__init__(*args, **kwargs)
        if project_pk is not None:
            self.fields['project'].queryset = Project.objects.filter(supervisor=user)
            self.fields['project'].initial = Project.objects.get(pk=project_pk[-37:-1])
        else:
            self.fields['project'].queryset = Project.objects.filter(supervisor=user)


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'coordinates': GooglePointFieldWidget,
        }
        labels = {
            "name": _("Name"),
            "coordinates": _(""),
            "street": _("Street"),
            "street_number": _("Street number"),
            "city": _("City"),
            "postal_code": _("Postal code"),
        }
