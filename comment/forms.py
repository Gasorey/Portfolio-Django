from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['name','empresa','email','commentary']
   
  def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      self.fields['name'].label = 'Nome'
      self.fields['empresa'].label = 'Empresa'
      self.fields['email'].label = 'E-mail'
      self.fields['commentary'].label = 'Comentário'


    


