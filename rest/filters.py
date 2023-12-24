from django.forms import DateInput
from django_filters import rest_framework as django_filters

from rest.models import Book, Author


class AuthorFilter(django_filters.FilterSet):
    # full_name = django_filters.CharFilter(
    #     field_name='full_name',
    #     lookup_expr='icontains'
    # )
    birth_date_after = django_filters.DateFilter(
        method='filter_birth_date_after',
        label='Birth Date',
        widget=DateInput(attrs={'placeholder': '1990-01-01'})
    )

    class Meta:
        model = Author
        fields = ('birth_date_after',)

    def filter_birth_date_after(self, queryset, name, value):
        return queryset.filter(birth_date__gt=value)


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.RangeFilter()
    author = django_filters.ModelChoiceFilter(
        queryset=Author.objects.all(),
        field_name='author',
        to_field_name='id',
        lookup_expr='exact'
    )
    description_and_year = django_filters.CharFilter(method='filter_by_description_and_year')

    class Meta:
        model = Book
        fields = ('name', 'year', 'author')

    def filter_by_description_and_year(self, queryset, name, value):
        parts = value.split(',')
        description = parts[0]
        year = parts[1]

        if description:
            queryset = queryset.filter(description__icontains=description)
        if year:
            queryset = queryset.filter(year=year)

        return queryset