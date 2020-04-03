from django.conf import settings
from .models import Publish

def context_publish(request):
  kwargs = {
    'publish_name': Publish.objects.all()
  }
  return kwargs