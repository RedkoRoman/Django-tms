from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    post_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('text', 'rating')
