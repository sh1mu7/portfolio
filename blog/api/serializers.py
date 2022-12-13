from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.models import Post, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'comment']



class PostSerializer(ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'slug', 'content', 'category', 'status', 'comments')
