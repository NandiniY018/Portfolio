"""
website/context_processors.py
Injects the global SiteSettings into all templates.
"""
from .models import SiteSettings, Resume

def site_settings(request):
    settings_obj = SiteSettings.objects.first()
    active_resume = Resume.objects.filter(is_active=True).first()
    
    # Auto-fix: If the DB expects a file that doesn't exist on disk, update it to the actual file on disk.
    if active_resume and active_resume.file:
        import os
        from django.conf import settings
        file_path = os.path.join(settings.MEDIA_ROOT, active_resume.file.name.replace('/', os.sep))
        if not os.path.exists(file_path):
            alt_path = os.path.join(settings.MEDIA_ROOT, 'resume', 'Nandini_Yamagar.pdf')
            if os.path.exists(alt_path):
                active_resume.file.name = 'resume/Nandini_Yamagar.pdf'
                active_resume.save()

    return {
        'site_settings': settings_obj,
        'active_resume': active_resume
    }
