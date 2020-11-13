from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import UserUpdateForm


@login_required
def user_update(request):
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
    return render(request, 'account/user_update.html', context)
