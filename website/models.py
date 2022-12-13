from django.contrib.auth import get_user_model
from blog.models import BaseModel
from django.db import models

User = get_user_model()


class About(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=100)
    work_email = models.EmailField()
    logo = models.ImageField(upload_to='website/logo/')
    bg_color = models.CharField(max_length=15, default='#282323')
    color = models.CharField(max_length=15, default='#00cb87')

    def __str__(self):
        return self.about[10]


class Project(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('COMPLETED', 'completed'),
        ('PUBLISH', 'publish'),
        ('ON-GOING', 'on-going'),
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
    duration = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return f'{self.title} {self.status}'


class Education(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('COMPLETED', 'completed'),
        ('ON-GOING', 'on-going')
    )
    degree = models.CharField(max_length=200, verbose_name='Achieved')
    institute = models.CharField(max_length=200)
    session = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return f'{self.degree} {self.institute}'


class Attribute(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)


class Skill(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='skill_attribute')
    domain = models.CharField(max_length=50, blank=False, null=False)

