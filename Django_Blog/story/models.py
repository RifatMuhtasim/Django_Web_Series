from django.db import models
from django.db.models.fields import TextField
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
 
class StoryPost(models.Model):
    StoryPostImage = models.ImageField(default= 'StoryPostImage.jpg', upload_to= 'StoryPost')
    StoryPostTitle = models.CharField(max_length=200)
    StoryPostAuthor = models.ForeignKey(User, on_delete= models.CASCADE)
    StoryPostTime = models.DateTimeField(default=timezone.now)
    StoryPostMetadata= RichTextField(blank= True, null= True)
    StoryPostBody1 = RichTextField(blank= True, null= True)
    StoryPostBodyImage = models.ImageField(default='StoryPost/BodyImage.jpg' , upload_to= "StoryPost/BodyImage")
    StoryPostBody2 = RichTextField(blank= True, null= True)
    StoryPostBody3 = RichTextField(blank= True, null= True)
    StoryPostUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.StoryPostTitle 
