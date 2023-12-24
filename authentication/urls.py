from django.urls import path, include

from rest_framework.routers import DefaultRouter

from authentication import views

app_name = 'authentication'
router = DefaultRouter()

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
router.register(r'users', views.CustomUserViewSet, basename='users')

urlpatterns += router.urls