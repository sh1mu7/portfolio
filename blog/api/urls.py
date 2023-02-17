from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..api import views

app_name = 'blog'
router = DefaultRouter()
router.register('tag', views.BlogPostViewSet, 'tag')
router.register('category', views.CategoryViewSet, 'category')
router.register('post', views.BlogPostViewSet, 'post')
router.register('comment', views.CommentViewSet, 'comment')
router.register('subscriber', views.Subscriber, 'subscriber')
urlpatterns = [
    path('', include(router.urls)),
]
