from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from core.models import UserWebsite, Project, EducationInformation, Skill
from core.utils import auth_utils


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs['email']
        try:
            user = auth_utils.get_user_by_email(email)
            auth_utils.validate_user(user)
            return attrs
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'email': [_(f"User with email {email} does not exist")]})


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebsite
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class EducationInformationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EducationInformation
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class SkillSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Skill
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
