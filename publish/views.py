from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PublishCreateForm
from publish.models import Publish
from django.urls import reverse, reverse_lazy


from django.utils import timezone


 

class ResumeView(TemplateView):
  template_name = 'publish/resume.html'

class PublishListView(ListView):
  model = Publish
  
  def get_queryset(self):
    qs = Publish.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    return qs
  
class PublishDetailView(DetailView):
  model = Publish

  def get_queryset(self):
    qs = Publish.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    return qs
  
class PublishCreateView(LoginRequiredMixin,CreateView):
  login_url = '/login'
  redirect_field_name = ''
  form_class = PublishCreateForm
  model = Publish

class PublishDeleteView(LoginRequiredMixin,DeleteView):
  model = Publish
  success_url = reverse_lazy('resume')

class PublishUpdateView(LoginRequiredMixin,UpdateView):
  model = Publish
  login_url = '/login'
  form_class = PublishCreateForm
  redirect_field_name = ''

