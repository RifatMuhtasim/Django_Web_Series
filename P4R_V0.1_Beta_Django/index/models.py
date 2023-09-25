from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE 


# Create your models here.

class HomePost(models.Model):
    HomePostTitle = models.CharField(max_length= 300)
    HomePostTime = models.DateTimeField(default= timezone.now)
    HomePostAuthor = models.ForeignKey(User, on_delete= models.CASCADE)
    HomePostMetadata = RichTextField(blank= True, null= True)
    HomePostImage = models.ImageField(default= 'HomePostImage.jpg', upload_to = 'HomePost')
    HomePostUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.HomePostTitle 