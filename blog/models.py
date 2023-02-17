from django.db import models
from django.utils.text import slugify
from core.models import BaseModel, User
from core.utils import optimizer


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Subscriber(BaseModel):
    email = models.EmailField(unique=True)
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class BlogPost(BaseModel):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    excerpt = models.TextField(verbose_name='Short Summary', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    featured_image = models.ImageField(upload_to='media/blogs/post/', null=True, default='static/media/default.png')
    thumbnail = models.ImageField(upload_to='media/blogs/post/thumbnail/', null=True,
                                  default='static/media/default.png')
    image_1 = models.ImageField(upload_to='media/blogs/post/', null=True, default='static/media/default.png')
    reference = models.TextField(null=True)
    meta_keyword = models.CharField(max_length=70, null=True)
    meta_description = models.CharField(max_length=165, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.featured_image:
            featured_image = optimizer.image_optimizer(self.featured_image)
            self.featured_image = featured_image
        if self.thumbnail:
            thumbnail = optimizer.thumb_generator(self.thumbnail)
            self.thumbnail = thumbnail
        if self.image_1:
            new_image = optimizer.image_optimizer(self.image_1)
            self.image_1 = new_image
        super(BlogPost, self).save(**kwargs)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(BlogPost, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name
