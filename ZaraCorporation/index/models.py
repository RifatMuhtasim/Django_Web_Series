from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from PIL import Image
# Create your models here.

class IndexBlog(models.Model):
        title   = models.CharField(max_length= 200)
        image = models.ImageField(default= 'default.jpg', upload_to= 'IndexImage')
        body = RichTextField(blank= True, null= True)
        time = models.DateTimeField(default = timezone.now)
        slug = models.SlugField(blank=True)

        def __str__(self):
                return f'Index:  {self.title}'

        def save(self, *args, **kwargs):
                super().save(*args, **kwargs)

                img= Image.open(self.image.path)
                if img.height > 300 or img.width>300:
                        output_size = (300, 300)
                        img.thumbnail(output_size)
                        img.save(self.image.path)
