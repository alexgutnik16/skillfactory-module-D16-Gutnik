from django.urls import path
from .views import PostsView, AdvertDetailView, AddAdvertView, ChangeAdvertView, CreateCommentView, \
    get_comments, accept_comment, delete_comment

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:pk>', AdvertDetailView.as_view()),
    path('add/', AddAdvertView.as_view()),
    path('change/<int:pk>', ChangeAdvertView.as_view(), name='change'),
    path('create_comment/', CreateCommentView.as_view()),
    path('my_comments/', get_comments),
    path('accept/<int:comment_id>', accept_comment, name='accept'),
    path('delete/<int:comment_id>', delete_comment, name='delete'),
]
