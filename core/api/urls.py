from django.urls import path
from .views import *
from rest_framework import routers

app_name = 'user'

router = routers.DefaultRouter()
router.register(prefix='website', viewset=WebsiteViewSet, basename='website')
router.register(prefix='project', viewset=ProjectViewSet, basename='project')
router.register(prefix='skill', viewset=SkillViewSet, basename='skill')
router.register(prefix='education', viewset=EducationViewSet, basename='education')
router.register(prefix='experience', viewset=ExperienceViewSet, basename='experience')
router.register(prefix='resume', viewset=ResumeViewSet, basename='resume')

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutViewSet.as_view(), name='logout')
]

urlpatterns += router.urls
