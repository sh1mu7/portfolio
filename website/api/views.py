from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .serializers import AboutSerializer, ProjectSerializer, EducationSerializer
from ..models import About, Project, Education


# About
class AboutListAPI(GenericAPIView, ListModelMixin):
    permission_classes = [AllowAny]
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AboutCreateAPI(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AboutUpdateAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AboutRetrieveAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AboutDeleteAPI(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Education
class EducationListAPI(GenericAPIView, ListModelMixin):
    permission_classes = [AllowAny]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EducationCreateAPI(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EducationUpdateAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class EducationRetrieveAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EducationDeleteAPI(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Project
class ProjectListAPI(GenericAPIView, ListModelMixin):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectCreateAPI(GenericAPIView, CreateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectUpdateAPI(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProjectRetrieveAPI(GenericAPIView, RetrieveModelMixin):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProjectDeleteAPI(GenericAPIView, DestroyModelMixin):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
