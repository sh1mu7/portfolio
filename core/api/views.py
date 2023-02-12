from urllib import request

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .serializers import LoginSerializer
from ..models import User, UserWebsite, Project, EducationInformation, Skill
from ..utils import auth_utils
from rest_framework import viewsets

from ..utils.auth_utils import get_user_by_email, regenerate_token


class LoginAPI(APIView):
    permission_classes = [AllowAny, ]

    @extend_schema(
        request=serializers.LoginSerializer,
        responses={200: serializers.LoginSerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'detail': "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        user = get_user_by_email(email)

        if not user:
            return Response({'detail': "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(serializer.validated_data['password']):
            return Response({'detail': "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, created = regenerate_token(user=user)
        data = {'email': 'Login Successfully', 'token': token.key}
        return Response(data, status=status.HTTP_200_OK)


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = UserWebsite.objects.all()
    serializer_class = serializers.WebsiteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        user = request.user
        user_website_info = UserWebsite.objects.filter(author=user)
        if user_website_info:
            return Response({"error": "You already created website information."})
        else:
            return super().create(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EducationInformationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EducationInformationSerializer
    queryset = EducationInformation.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SkillSerializer
    queryset = Skill.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
