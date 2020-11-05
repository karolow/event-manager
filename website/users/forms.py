from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm

from .models import CustomUser
from organizations.models import Organization


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('position', 'phone',)
        fields = (
            'position',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
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
