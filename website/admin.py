from django.contrib import admin
from .models import (
    ContactMessage, Project, ProjectImage, Skill, Experience, Education, Article, SiteSettings, Certificate, Resume
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3
    max_num = 10
    fields = ('image', 'caption', 'order')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [ProjectImageInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'category_order', 'order', 'percentage', 'icon_color')
    list_editable = ('category_order', 'order', 'percentage', 'icon_color')
    list_filter = ('category',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'order')
    list_editable = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'order')
    list_editable = ('order',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'order')
    list_editable = ('order',)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin interface for viewing contact form submissions."""
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)
    list_per_page = 25

    def has_add_permission(self, request):
        # Messages are submitted via the contact form only
        return False

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'institution', 'order')
    list_editable = ('order',)
    list_filter = ('category',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active', 'uploaded_at')
    list_filter = ('is_active',)

