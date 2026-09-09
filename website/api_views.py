from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Project, Skill, Experience, Education, Article, Certificate
from .serializers import (
    ProjectSerializer, SkillSerializer, ExperienceSerializer, 
    EducationSerializer, ArticleSerializer, CertificateSerializer
)

class CachedModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions
    and caches the output for 15 minutes.
    """
    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProjectViewSet(CachedModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(CachedModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(CachedModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(CachedModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ArticleViewSet(CachedModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CertificateViewSet(CachedModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
