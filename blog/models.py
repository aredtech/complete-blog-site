from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.
from django.conf import settings

#To Override default user
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Model for New User Profile """

    def create_user(self, email, name, password=None):
        """New Normal User"""
        if not email:
            raise ValueError("User must have a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    

    def create_superuser(self, email, name, password):
        """For New Super User"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Model for Users in DB """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name
        
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural= "Users"

class Tags(models.Model):
    tag = models.CharField(max_length=20)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    author_email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images")


class Comment(models.Model):
    text = models.TextField()

class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

