from time import sleep

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control
from django_filters import rest_framework as django_filters
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest.filters import BookFilter, AuthorFilter
from rest.middleware import BeforeRequestMiddleware, AfterRequestMiddleware
from rest.models import Book, Author
from rest.pagination import BookPagination
from rest.permissions import IsPaidUserPermission, IsAdminUpdatePermission
from rest.serializers import (
    BookListSerializer,
    BookRetrieveSerializer,
    BookCreateSerializer,
    BookUpdateSerializer,
    BookRecentBooksSerializer,
    BookImageUpdateSerializer,
    AuthorsSerializer,
)
from rest.services import BookService


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = BookFilter
    ordering_fields = ('id', 'name', 'year', 'author')
    ordering = ('-id', )
    search_fields = ('name', 'year', 'author__last_name', 'author__first_name')
    pagination_class = BookPagination
    permission_classes = (IsAuthenticated, IsPaidUserPermission, IsAdminUpdatePermission)
    serializer_classes = {
        'list': BookListSerializer,
        'create': BookCreateSerializer,
        'retrieve': BookRetrieveSerializer,
        'update': BookUpdateSerializer,
        'partial_update': BookUpdateSerializer,
        'recent_books': BookRecentBooksSerializer,
        'update_image': BookImageUpdateSerializer,
        'paid_books': BookListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    # @swagger_auto_schema(
    #     responses={200: BookListSerializer(many=True)},
    #     operation_description='Returns all books with additional filters and ordering'
    # )
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # @swagger_serializer_method(serializer_or_field=BookCreateSerializer)
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        book.is_deleted = True
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='recent-books')
    def recent_books(self, request):
        recent_books = Book.objects.filter(year__gte=2020)
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(recent_books, many=True)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     request_body=BookImageUpdateSerializer,
    #     responses={200: BookImageUpdateSerializer()},
    #     operation_description='Update Image of a specific book'
    # )
    @action(detail=True, methods=['patch'], url_path='update-image')
    def update_image(self, request, pk=None):
        book = self.get_object()
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(book, request.data, partial=True)

        BookService.update_image(serializer=serializer, instance=book, request=request)

        self.perform_update(serializer)

        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='paid-books')
    def paid_books(self, request):
        # if not request.user.is_paid:
        #     return Response({'message': 'you can\'t to do it'}, status=status.HTTP_403_FORBIDDEN)
        paid_books = Book.objects.filter(is_free=False)
        serializer = self.get_serializer_class()(paid_books, many=True)
        return Response(serializer.data)


# @method_decorator(BeforeRequestMiddleware, name='dispatch')
# @method_decorator(AfterRequestMiddleware, name='dispatch')
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = AuthorFilter

    # @method_decorator(cache_page(10))
    # @method_decorator(cache_control(max_age=15, no_cache=True, no_store=True))
    def list(self, request, *args, **kwargs):
        # sleep(5)
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get'], url_path='books')
    def books(self, request, pk=None):
        author = self.get_object()
        books = author.books.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)