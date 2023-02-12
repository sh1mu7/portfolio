from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from .managers import PostObjects
from core.models import BaseModel
User = get_user_model()


# Create your models here.



class Tag(BaseModel):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='tag/%Y/%m/%d')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.image.name = 'tag/%s_%s' % (slugify(self.name), self.image.name.split('/')[-1])
        super().save(*args, **kwargs)
