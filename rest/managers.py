from django.db import models


class BookManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class DeletedBookManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)
