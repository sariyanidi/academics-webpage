def context_personal_settings(request):
    """Insert some additional information into the template context
    from the settings.
    Specifically, the LOGOUT_URL, MEDIA_URL and BADGES settings.
    """
    from django.conf import settings
    additions = {
        'MEDIA_URL': settings.MEDIA_URL,
        'LOGOUT_URL': settings.LOGOUT_URL,
        'BASE_URL' : settings.BASE_URL
    }
    return additions
