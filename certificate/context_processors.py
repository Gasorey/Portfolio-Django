from django.conf import settings
from .models import Certificate

def context_certificate(request):
  kwargs = {
    'certificate_name': Certificate.objects.all()
  }
  return kwargs