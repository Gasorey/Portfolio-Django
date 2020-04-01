from django.db import models
import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Publish(models.Model):
  user = models.ForeignKey(User,null=True, on_delete=models.CASCADE )
  author = models.CharField(max_length=256, null= True)
  publish_name = models.CharField(max_length=256, null = True)
  description = models.TextField()
  create_date = models.DateTimeField(default=timezone.now)
  

  def published(self):
    self.create_date = timezone.now()
    self.save()
  
  def get_absolute_url(self):
    return reverse('publish_list')

  # def __str__(self):
  #   self.publish_name
  