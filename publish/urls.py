from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path('',views.ResumeView.as_view(),name='resume'),
  path('publish/',views.PublishListView.as_view(),name='publish_list'),
  path('new/',views.PublishCreateView.as_view(),name='publish_form'),
  path('accounts/logout',LogoutView.as_view(),name='logout',kwargs={'next_page':''}),
  path('publish/<int:pk>/',views.PublishDetailView.as_view(),name='publish_detail'),
  path('publish/<int:pk>/delete',views.PublishDeleteView.as_view(),name='publish_delete'),
  path('publish/<int:pk>/update',views.PublishUpdateView.as_view(),name='publish_update'),

 
]