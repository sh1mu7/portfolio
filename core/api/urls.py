from django.urls import path
from .views import *
from rest_framework import routers

app_name = 'user'

router = routers.DefaultRouter()
router.register(prefix='website', viewset=WebsiteViewSet, basename='website')
router.register(prefix='project', viewset=ProjectViewSet, basename='project')
router.register(prefix='education-information', viewset=EducationInformationViewSet, basename='education-information')
router.register(prefix='skill', viewset=SkillViewSet, basename='skill')
urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
]+router.urls
