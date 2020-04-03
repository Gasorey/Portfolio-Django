from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Certificate(models.Model):
  user = models.ForeignKey(User,null=True, on_delete=models.CASCADE )
  org = models.CharField(max_length=256, null= True)
  name = models.CharField(max_length=256, null = True)
  description = models.TextField(null=True)
  create_date = models.DateTimeField(null = True)
  photo = models.ImageField(upload_to='certificate/image', null=True, blank=True)

  def image (self):
    self.photo.save()    

  @property
  def photo_url(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url
  
  def get_absolute_url(self):
    return reverse('resume')
