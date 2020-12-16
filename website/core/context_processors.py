from django.conf import settings


def any_user(request):
    kwargs = {
        'project_name': settings.PROJECT_NAME,
        'contact_email': settings.CONTACT_EMAIL,
    }
    return kwargs


def authenticated_user(request):
    if request.user.is_authenticated:
        try:
            kwargs = {
                'organization_name': request.user.organization.short_name,
            }
        except AttributeError:
            kwargs = {
                'organization_name': 'Event Manager',
            }
        return kwargs
    else:
        return {}
