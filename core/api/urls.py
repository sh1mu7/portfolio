from django.urls import path
from .views import *
from rest_framework import routers

app_name = 'user'

router = routers.DefaultRouter()
router.register(prefix='website', viewset=WebsiteViewSet, basename='website')
urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
]+router.urls
