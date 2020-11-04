from django.conf import settings


def contact_email_context_processor(request):
    kwargs = {
        'contact_email': settings.CONTACT_EMAIL,
        'project_name': settings.PROJECT_NAME,
        'organization_name': request.user.organization,
    }
    return kwargs
