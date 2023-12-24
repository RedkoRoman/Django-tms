from rest_framework.routers import DefaultRouter

from rest import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')
router.register(r'authors', views.AuthorViewSet, basename='authors')

urlpatterns = router.urls