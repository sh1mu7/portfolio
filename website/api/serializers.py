from rest_framework.serializers import ModelSerializer
from ..models import About, Project, Education


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


