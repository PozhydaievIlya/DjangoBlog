from django import forms
from .models import Post, UsersEmail, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'tags')


class UsersForm(forms.ModelForm):
    class Meta:
        model = UsersEmail
        fields = ["user_email"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['username', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

