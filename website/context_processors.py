"""
website/context_processors.py
Injects the global SiteSettings into all templates.
"""
from .models import SiteSettings, Resume

def site_settings(request):
    settings_obj = SiteSettings.objects.first()
    active_resume = Resume.objects.filter(is_active=True).first()
    return {
        'site_settings': settings_obj,
        'active_resume': active_resume
    }
