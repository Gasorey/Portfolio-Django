from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import DetailView, ListView, DeleteView, CreateView, TemplateView, UpdateView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PublishCreateForm
from publish.models import Publish
from django.urls import reverse, reverse_lazy


# Create your views here.

def publish_list(request):
  queryset = Publish.objects.all()
  context = {
    "object_list": queryset
  }
  return render(request,context)



class ResumeView(TemplateView):
  template_name = 'publish/resume.html'

class PublishListView(ListView):
  model = Publish
  
  def get_queryset(self):
    qs = Publish.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    return qs
  
  
class PublishDetailView(DetailView):
  model = Publish

class PublishCreateView(LoginRequiredMixin,CreateView):
  login_url = '/login'
  redirect_field_name = ''
  form_class = PublishCreateForm
  model = Publish

class PublishDeleteView(LoginRequiredMixin,DeleteView):
  model = Publish
  success_url = reverse_lazy('')

class PublishUpdateView(LoginRequiredMixin,UpdateView):
  model = Publish
  login_url = '/login'
  form_class = PublishCreateForm
  redirect_field_name = ''