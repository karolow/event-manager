from django.conf import settings


def contact_email_context_processor(request):
    kwargs = {
        'contact_email': settings.CONTACT_EMAIL,
    }
    return kwargs
