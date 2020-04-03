from django.urls import path, include
from . import views


urlpatterns = [
  
  path('certificate/',views.CertificateListView.as_view(),name='certificate_list'),
  path('new_certificate/',views.CertificateCreateView.as_view(),name='certificate_form'),
  path('certificate/<int:pk>/',views.CertificateDetailView.as_view(),name='certificate_detail'),
  path('certificate/<int:pk>/delete',views.CertificateDeleteView.as_view(),name='certificate_delete'),
  path('certificate/<int:pk>/update',views.CertificateUpdateView.as_view(),name='certificate_update'),
]