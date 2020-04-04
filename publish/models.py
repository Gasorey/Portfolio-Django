from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User




class Publish(models.Model):
  user = models.ForeignKey(User,null=True, on_delete=models.CASCADE )
  author = models.CharField(max_length=256, null= True)
  name = models.CharField(max_length=256, null = True)
  github = models.CharField(max_length=256,null=True, blank = True)
  tech = models.CharField(max_length=500, null=True, blank = True)
  description = models.TextField()
  create_date = models.DateTimeField(default=timezone.now)
  

  def published(self):
    self.create_date = timezone.now()
    self.save()
  
  def get_absolute_url(self):
    return reverse('resume')

  # def __str__(self):
  #   self.publish_name
  