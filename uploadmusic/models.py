from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
import uuid
# Create your models here.




class Uploadmusic(models.Model):
    key = models.SlugField()
    adamid=models.SlugField()
    lyrics = models.TextField()
    ky = models.SlugField()
    image = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=100)
    track = models.FileField(upload_to='music/')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField()
    title = models.CharField(max_length=100 , blank=True , null=True)
    description = models.TextField(max_length=100 , blank=True , null=True)
    
    class Meta:
        unique_together = ['track', 'title' , "id"]
        ordering = ['title']
        
    def __str__(self):
        return f'{self.title}'
        
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
  
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url
        return ''
    
    def tracks(self):
        if self.track:
            return 'http://127.0.0.1:8000/' + self.track.url
        return ''
    

   
   
