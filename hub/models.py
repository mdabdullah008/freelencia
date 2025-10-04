from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('freelancer', 'Freelancer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    name = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField('Category', blank=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):

        return self.user.username

#Programming & Tech Table
class ProgrammingTech(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/')
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)

def __str__(self):
    return self.name

#Graphics & Design Table
class GraphicsDesign(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/')
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)

def __str__(self):
    return self.name

#Video & Animation Table
class VideoAnimation(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/')
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)

def __str__(self):
    return self.name

#Business Table
class Business(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/')
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)

def __str__(self):
    return self.name