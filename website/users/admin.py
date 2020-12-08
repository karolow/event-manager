from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Groups'

    list_display = ['email', 'username', 'position', 'is_staff', 'group']

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',
                           'last_name', 'password', 'organization', 'position', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'position', 'phone', 'organization')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
