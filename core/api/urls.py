from django.urls import path
from .views import LoginAPI

app_name = 'user'

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),

]
