from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Tag, Category, BlogPost, Comment, Subscriber
from blog.utility.blog_post import create_blog_post


class TagSerializer(ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Tag
        exclude = ('id',)


class CategorySerializer(ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment', 'post')


class BlogPostSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tags = TagSerializer(many=True, read_only=False)
    category = CategorySerializer(many=False, read_only=False)

    class Meta:
        model = BlogPost
        fields = '__all__'

    def create(self, validated_data):
        post = create_blog_post(validated_data)
        return post


class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'
