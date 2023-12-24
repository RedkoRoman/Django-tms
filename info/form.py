from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from info.models import InfoBlog


class InfoBlogForm(forms.ModelForm):
    class Meta:
        model = InfoBlog
        fields = ('name', 'text', 'rating', 'price')


# class InfoBlogAccessDateUpdateForm(forms.Form):
#     new_access_date = forms.DateField(help_text='Enter a new access date', required=True)
#
#     def clean_new_access_date(self):
#         data = self.cleaned_data['new_access_date']  # {'new_access_date': '2023-11-02'}
#         if data < timezone.now().date():
#             raise ValidationError('Invalid date - your date is in the past')
#         return data


class InfoBlogAccessDateUpdateForm(forms.ModelForm):
    class Meta:
        model = InfoBlog
        fields = ('access_date',)

    def clean_access_date(self):
        data = self.cleaned_data['access_date']  # {'access_date': '2023-11-02'}
        if data < timezone.now().date():
            raise ValidationError('Invalid date - your date is in the past')
        return data