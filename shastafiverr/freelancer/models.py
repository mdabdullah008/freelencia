from django.db import models
from django.auth.contrib.models import User

# Create your models here.

class UserProfieInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):

        return self.user.username