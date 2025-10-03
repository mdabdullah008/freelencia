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


    def __str__(self):

        return self.user.username
