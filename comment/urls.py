from django.urls import path, include
from . import views

urlpatterns = [
  path('',views.CommentCreateView.as_view(),name='create_comment'),
  path('comment_list/',views.CommentListView.as_view(),name='list_comment'),
  path('comment/<int:pk>/',views.CommentDetailView.as_view(),name='comment_detail'),
  path('comment/<int:pk>/delete',views.CommentDeleteView.as_view(),name='comment_delete'),
  path('comment/<int:pk>/update',views.CommentUpdateView.as_view(),name='comment_update'),
  path('thanks/',views.CommentObrigadoView.as_view(),name='obrigado'),
]