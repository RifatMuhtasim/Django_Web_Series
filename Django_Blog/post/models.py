from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class StartPost(models.Model):
    Title = models.CharField(max_length=200)
    Body = RichTextField(blank= True, null= True)
    Image = models.ImageField(default='StartPostImage.jpg' , upload_to= "StartPostImage")
    StartPostAuthor= models.ForeignKey(User , on_delete= models.CASCADE )
    StartPostTime= models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.Title

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-detail-post', kwargs={'pk': self.pk})