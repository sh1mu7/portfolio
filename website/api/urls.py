from django.template.defaulttags import url
from django.urls import path

from ..api import views

app_name = 'website'
urlpatterns = [
    path('about/create', views.AboutCreateAPI.as_view(), name='about-create'),
    path('about/', views.AboutListAPI.as_view(), name='about-list'),
    path('about/details/<slug:slug>', views.AboutRetrieveAPI.as_view(), name='about-details'),
    path('about/update/<slug:slug>', views.AboutUpdateAPI.as_view(), name='about-update'),
    path('about/delete/<slug:slug>', views.AboutDeleteAPI.as_view(), name='about-delete'),

    path('education/', views.EducationListAPI.as_view(), name='education-list'),
    path('education/create', views.EducationCreateAPI.as_view(), name='education-create'),
    path('education/details/<slug:slug>', views.EducationRetrieveAPI.as_view(), name='education-details'),
    path('education/update/<slug:slug>', views.EducationUpdateAPI.as_view(), name='education-update'),
    path('education/delete/<slug:slug>', views.EducationDeleteAPI.as_view(), name='education-delete'),

    path('project/create', views.ProjectCreateAPI.as_view(), name='project-create'),
    path('project/', views.ProjectListAPI.as_view(), name='project-list'),
    path('project/details/<slug:slug>', views.ProjectRetrieveAPI.as_view(), name='project-details'),
    path('project/update/<slug:slug>', views.ProjectUpdateAPI.as_view(), name='project-update'),
    path('project/delete/<slug:slug>', views.ProjectDeleteAPI.as_view(), name='project-delete'),


]
