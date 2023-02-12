from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import MyUserManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(unique=True, max_length=20)
    dob = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    REQUIRED_FIELDS = ['mobile']

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class UserWebsite(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    website_url = models.CharField(max_length=100)
    website_name = models.CharField(max_length=100)
    objectives = models.TextField(null=True)
    about = models.TextField(null=True)
    logo = models.ImageField(upload_to='website_logos/%Y/%m/%d/', null=True)
    bg_color = models.CharField(help_text='color_code: #000000', max_length=7, null=True)
    font_color = models.CharField(help_text='color_code: #000000', max_length=7, null=True)
    font_url = models.CharField(max_length=300, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    github_link = models.CharField(max_length=200, null=True)
    linkedin_link = models.CharField(max_length=200, null=True)

    class Meta:
        permissions = [
            ("view_website", "Can view website information"),
        ]

    def save(self, *args, **kwargs):
        if not self.pk and not self.author.is_superuser:
            raise PermissionError("Only superusers can create websites")
        elif not self.author.is_superuser:
            raise PermissionError("Only superusers can update or delete websites")
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.website_name

class Project(models.Model):
    user = models.ManyToManyField(User, related_name='user')
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    source_link=models.URLField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class EducationInformation(BaseModel):
    user = models.ManyToManyField(User, related_name='user')
    certification_name = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.certification_name


class SkillAttribute(BaseModel):
    name = models.CharField(max_length=30)


class Skills(BaseModel):
    user = models.ManyToManyField(User, related_name='skills')
    skill_name = models.CharField(max_length=100)
    skill_attribute = models.ForeignKey(SkillAttribute, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, null=True, help_text='on scale of 10')
    years_of_experience = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.skill_name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Resume(BaseModel):
    file = models.FileField(upload_to='Resume')

    def __str__(self):
        return self.file.name
