"""
portfolio/urls.py
Root URL configuration for the Portfolio project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from website import api_views

router = DefaultRouter()
router.register(r'projects', api_views.ProjectViewSet)
router.register(r'skills', api_views.SkillViewSet)
router.register(r'experience', api_views.ExperienceViewSet)
router.register(r'education', api_views.EducationViewSet)
router.register(r'articles', api_views.ArticleViewSet)
router.register(r'certificates', api_views.CertificateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', include('website.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
