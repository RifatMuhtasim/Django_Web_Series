from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class blog(models.Model):
        image = models.ImageField(default = 'default.jpg', upload_to = 'loadimg')
        title = models.CharField(max_length= 200)
        author = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
        time = models.DateTimeField(default = timezone.now)
        meta = models.TextField( blank= True, null= True)
        body = RichTextField(null=True, blank=True)
        url = models.CharField(max_length = 200)
        slug = models.SlugField(blank=True)

        def __str__(self):
                return self.title

        # def get_absolute_url(self):
        #         return reverse('BlogDetail', kwargs={'pk': self.pk})