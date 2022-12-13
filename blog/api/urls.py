from django.urls import path
from ..api import views

app_name = 'blog_api'

urlpatterns = [
    path('post/create', views.PostCreateAPI.as_view(), name='post-create'),
    path('post/', views.PostListAPI.as_view(), name='post-list'),
    path('post/details/<slug:slug>', views.PostRetrieveAPI.as_view(), name='post-details'),
    path('post/update/<slug:slug>', views.PostUpdateAPI.as_view(), name='post-update'),
    path('post/update/<slug:slug>', views.PostDeleteAPI.as_view(), name='post-delete'),

    path('tags/create', views.CategoryCreateAPI.as_view(), name='category-create'),
    path('tags/', views.CategoryListAPI.as_view(), name='category-list'),
    path('tags/details/<int:pk>', views.CategoryRetrieveAPI.as_view(), name='category-details'),
    path('tags/update/<int:pk>', views.CategoryUpdateAPI.as_view(), name='category-update'),
    path('tags/delete/<int:pk>', views.CategoryDeleteAPI.as_view(), name='category-delete'),

    path('comment/create', views.CommentCreateAPI.as_view(), name='comment-create'),
    path('comment/', views.CommentListAPI.as_view(), name='comment-list'),
    path('comment/details/<int:pk>', views.CommentRetrieveAPI.as_view(), name='comment-details'),
    path('comment/update/<int:pk>', views.CommentUpdateAPI.as_view(), name='comment-update'),
    path('comment/delete/<int:pk>', views.CommentDeleteAPI.as_view(), name='comment-delete')

]
