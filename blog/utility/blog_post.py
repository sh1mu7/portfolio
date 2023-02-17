from django.conf import settings
from django.db import transaction

from blog.models import Category, Subscriber, BlogPost,Tag
from core.utils.auth_utils import send_email


def create_blog_post(validated_data):
    tags_data = validated_data.pop('tags')
    category_data = validated_data.pop('category')

    with transaction.atomic():
        category, created = Category.objects.get_or_create(name=category_data['name'])
        post = BlogPost.objects.create(category=category, **validated_data)
        tags = []
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            tags.append(tag)
        post.tags.set(tags)

    subscribers = Subscriber.objects.all()
    recipient_list = [subscriber.email for subscriber in subscribers]
    subject = 'New Blog Post: {}'.format(post.title)
    message = 'Hi there,\n\nA new blog post has been published: {}.\n\nCheck it out here: {}'.format(post.title,
                                                                                                      settings.BASE_URL)
    send_email(subject, message, recipient_list)

    return post

