from rest_framework import serializers

from rest.models import Book, Author


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'author_name', 'image', 'is_deleted')
        read_only_fields = ('author_name', )

    def get_author_name(self, obj):
        return obj.author.full_name


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'description', 'author', 'image')


class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'description', 'author',)


class BookImageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('image', )


class BookRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer()

    class Meta:
        model = Book
        fields = ('id', 'name', 'year', 'description', 'author', 'image')
        extra_kwargs = {
            'author': {'write_only': True},
        }


class BookRecentBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name')