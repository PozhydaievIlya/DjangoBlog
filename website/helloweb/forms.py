from django import forms
from .models import Post, UsersEmail, Comments, Profile


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
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]



