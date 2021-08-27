from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    ProfileImage = models.ImageField(default='ProfileImage.jpg', upload_to='ProfileImage')

    def __str__(self):
        return f'{self.user} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
