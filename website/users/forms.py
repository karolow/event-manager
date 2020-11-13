from .models import *
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm

from organizations.models import Organization


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields + ('position', 'phone',)
        fields = (
            'position',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = UserChangeForm.Meta.fields


class ExtendedSignupForm(SignupForm):
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        empty_label="Select your organization"
    )

    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.organization = self.cleaned_data['organization']
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'position',
        )
        labels = {
            "first_name": _("First name"),
            "last_name": _("Last name"),
            "email": _("Email"),
            "phone": _("Phone"),
            "position": _("Position"),
        }
