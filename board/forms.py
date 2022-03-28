from django.forms import ModelForm
from .models import Advert, Comment


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['author', 'heading', 'text', 'category', 'upload']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'advert_comment', 'author_comment']
