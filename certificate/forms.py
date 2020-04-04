from django import forms
from .models import Certificate

class CertificateCreateForm(forms.ModelForm):
  class Meta:
    model = Certificate
    fields = ['user','org','name','description','tech','create_date','photo']