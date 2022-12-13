from django.db import models


class PostObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')



