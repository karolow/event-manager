from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from allauth.account.views import PasswordChangeView
from rest_framework.authtoken.models import Token

from .forms import UserUpdateForm


@login_required
def account_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('event_table')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'account/account_update.html', context)


class CustomPasswordChangeView(LoginRequiredMixin,
                               PasswordChangeView):

    def get_success_url(self):
        return reverse('event_table')


class APIManagementView(LoginRequiredMixin,
                        TemplateView):
    template_name = 'account/account_api.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['token'] = Token.objects.get(user=self.request.user)
        return context
