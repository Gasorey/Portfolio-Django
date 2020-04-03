from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CertificateCreateForm
from certificate.models import Certificate
from django.urls import reverse, reverse_lazy

from django.utils import timezone
# Create your views here.

class CertificateListView(ListView):
  model = Certificate
  
  def get_queryset(self):
    qs = Certificate.objects.all()
    return qs
  
class CertificateDetailView(DetailView):
  model = Certificate

  def get_queryset(self):
    qs = Certificate.objects.all()
    return qs
  
class CertificateCreateView(LoginRequiredMixin,CreateView):
  login_url = '/login'
  redirect_field_name = ''
  form_class = CertificateCreateForm
  model = Certificate

class CertificateDeleteView(LoginRequiredMixin,DeleteView):
  model = Certificate
  success_url = reverse_lazy('resume')

class CertificateUpdateView(LoginRequiredMixin,UpdateView):
  model = Certificate
  login_url = '/login'
  form_class = CertificateCreateForm
  redirect_field_name = 'resume'
