from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import MyUserManager
from .utils import optimizer


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

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


class Website(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    website_url = models.CharField(max_length=100)
    website_name = models.CharField(max_length=100)
    about = models.TextField(null=True)
    about_excerpt = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='media/website_logos/%Y/%m/%d/', null=True, default='static/media/logo.png')
    bg_color = models.CharField(help_text='color_code: #000000', max_length=7, null=True, default='#0d1117')
    font_color = models.CharField(help_text='color_code: #000000', max_length=7, null=True, default='#00cb87')
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
        ordering = ['-created_at']
        permissions = [
            ("view_site_info", "Can view website information"),
        ]

    def save(self, *args, **kwargs):
        if not self.pk and not self.author.is_superuser:
            raise PermissionError("Only superusers can create websites")
        elif not self.author.is_superuser:
            raise PermissionError("Only superusers can update or delete websites")
        if self.logo:
            new_logo = optimizer.image_optimizer(self.logo)
            self.image = new_logo
        super().save(**kwargs)

    def __str__(self):
        return self.website_name


class Project(BaseModel):
    user = models.ForeignKey(User, related_name='project', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='media/projects', null=True, default='static/media/default.webp')
    thumbnail = models.ImageField(upload_to='media/projects/thumbnail', null=True,
                                  default='static/media/default.webp')
    live_url = models.URLField(null=True)
    source_link = models.URLField(null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.image:
            new_image = optimizer.image_optimizer(self.image)
            self.image = new_image
        if self.thumbnail:
            new_thumbnail = optimizer.thumb_generator(self.thumbnail)
            self.thumbnail = new_thumbnail
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Skill(BaseModel):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    technology = models.CharField(max_length=300)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.skill_name


class Education(BaseModel):
    user = models.ForeignKey(User, related_name='education', on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.degree_name


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True)
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Resume(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    file = models.FileField(upload_to='media/resume/temp', default='static/media/resume.pdf')
    version = models.PositiveIntegerField()

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_resume = Resume.objects.get(pk=self.pk)
            if old_resume.file != self.file:
                self.version = old_resume.version + 1
        super().save(*args, **kwargs)
