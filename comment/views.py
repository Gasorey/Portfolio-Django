from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView, DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentCreateForm
from comment.models import Comment
from django.urls import reverse, reverse_lazy
from django.utils import timezone

class CommentObrigadoView(TemplateView):
  template_name = 'comment/obrigado.html'

class CommentListView(ListView):
  model = Comment
  
  def get_queryset(self):
    qs = Comment.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    return qs
  
class CommentDetailView(DetailView):
  model = Comment

  def get_queryset(self):
    qs = Comment.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
    return qs
  
class CommentCreateView(CreateView):
  login_url = '/login'
  redirect_field_name = ''
  form_class = CommentCreateForm
  model = Comment

class CommentDeleteView(LoginRequiredMixin,DeleteView):
  model = Comment
  success_url = reverse_lazy('resume')

class CommentUpdateView(LoginRequiredMixin,UpdateView):
  model = Comment
  login_url = '/login'
  form_class = CommentCreateForm
  redirect_field_name = ''