from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from .managers import PostObjects

User = get_user_model()


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Post(BaseModel):
    options = (
        ('published', 'published'),
        ('draft', 'draft')
    )
    category = models.ManyToManyField(Category, default='NGINX')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=300, blank=False, null=False)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()
    PostObjects = PostObjects()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    def __str__(self):
        return f'{self.email} {self.comment[:10]}'
