from django.urls import path

from info import views

urlpatterns = [
    path('test/', views.read_post, name='test'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update-access-date', views.PostAccessDateUpdateView.as_view(), name='post-access-date-update'),
]