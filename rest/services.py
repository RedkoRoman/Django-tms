class AuthorService:
    pass


class BookService:

    @staticmethod
    def _update_fields():
        pass

    @staticmethod
    def update_image(serializer, instance, request):
        BookService._update_fields()
        if serializer.is_valid(raise_exception=True):
            instance.image.delete(save=True)
            instance.image = request.data['image']