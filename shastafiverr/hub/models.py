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
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):

        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):

        return self.name


class Job(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client_jobs")
    
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="freelancer_jobs")
    
    title = models.CharField(max_length=200)
    
    description = models.TextField()
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
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

class ClientRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('cancelled', 'Cancelled')
    ]
    
    title = models.CharField(max_length=200)
    freelancer = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    email = models.EmailField()
    details = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Request from {self.client.username} to {self.freelancer.username} ({self.status})"