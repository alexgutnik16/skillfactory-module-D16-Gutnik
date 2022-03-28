from django_filters import FilterSet
from .models import Comment


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'advert_comment__heading': ['icontains'],
            'accepted': ['exact']
        }
