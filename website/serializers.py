from rest_framework import serializers
from .models import Project, Skill, Experience, Education, Article, Certificate

class ProjectSerializer(serializers.ModelSerializer):
    features_list = serializers.ListField(child=serializers.CharField(), source='get_features_list', read_only=True)
    tech_stack_list = serializers.ListField(child=serializers.CharField(), source='get_tech_stack_list', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    description_list = serializers.ListField(child=serializers.CharField(), source='get_description_list', read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tags_list = serializers.ListField(child=serializers.CharField(), source='get_tags_list', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    tech_stack_list = serializers.ListField(child=serializers.CharField(), source='get_tech_stack_list', read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__'
