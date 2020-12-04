from .models import *
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm

from organizations.models import Organization

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        # fields = UserCreationForm.Meta.fields + ('position', 'phone',)
        fields = (
            'position',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields


class ExtendedSignupForm(SignupForm):
    organization_queryset = Organization.objects.all()
    organization = forms.ModelChoiceField(
        queryset=organization_queryset,
        empty_label=_('Select your organization')
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean(self):
        """
        Check signup email domain against organization's
        allowed domain list
        """
        cleaned_data = super(ExtendedSignupForm, self).clean()
        organization = cleaned_data.get("organization")
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _('Account with this email already exists')
            )
        email_domain = email.split('@')[-1]

        if str(organization) != "Other":
            domains = self.organization_queryset.get(
                title=organization).email_domain
            if domains == '':
                raise forms.ValidationError(
                    _('Sorry, it seems that at the moment this organization does not accept new users')
                )
            else:
                domains_list = domains.replace(' ', '').split(',')

                if email_domain not in domains_list:
                    if len(domains_list) == 1:
                        raise forms.ValidationError(
                            _('Your email address has to be in {} domain').format(domains_list)
                        )
                    else:
                        domains_list = ', '.join(domains_list)
                        raise forms.ValidationError(
                            _('Your email address has to be in one of these domains: {}').format(domains_list)
                        )

    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.organization = self.cleaned_data['organization']
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
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
