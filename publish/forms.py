from django import forms
from .models import Publish

class PublishCreateForm(forms.ModelForm):
  class Meta:
    model = Publish
    fields = ['user','author','name','description','tech','github']
    


