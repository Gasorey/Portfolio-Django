from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model): 
  name = models.CharField(max_length=256, null = True)
  empresa = models.CharField(max_length=256,null=True,blank=True)
  email = models.EmailField(null=True,blank=True)
  commentary = models.TextField()
  create_date = models.DateTimeField(default=timezone.now)
  
  

  def published(self):
    self.create_date = timezone.now()
    self.save()
  
  def get_absolute_url(self):
    return reverse('obrigado')
