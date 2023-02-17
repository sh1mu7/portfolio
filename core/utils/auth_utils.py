from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from ..models import User


def regenerate_token(user):
    token, created = Token.objects.get_or_create(user=user)
    if not created:
        token.delete()
    return Token.objects.get_or_create(user=user)


def get_client_info(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    return ip, user_agent


def get_user_by_email(email):
    return User.objects.get(email=email)


def validate_user(user):
    if not user.is_staff and user.is_superuser:
        raise serializers.ValidationError({'email': 'You are unauthorized to perform action'})


def send_email(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
    )
