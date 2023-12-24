from celery import shared_task

from rest.models import Book


@shared_task
def delete_deleted_books():
    deleted_books = Book.deleted_objects.all()  # is_deleted = True
    deleted_books.delete()