from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(default='default.jpg', upload_to='profile_pics')


class ImageUploader(models.Model):
        image_name = models.CharField(max_length=100)
        image = models.ImageField(upload_to='Images')
        user = models.CharField(max_length=100) 
        user_profile = models.CharField(max_length=100)
        date = models.DateField()