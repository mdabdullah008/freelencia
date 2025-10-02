from django.db import models
from django.contrib.auth.models import User

# Create your models here please.

class UserProfileInfo(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('freelancer', 'Freelancer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):

        return self.user.username
