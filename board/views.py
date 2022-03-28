from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Advert, Comment
from .forms import AdvertForm, CommentForm
from .filters import CommentFilter


@login_required
def get_comments(request):
    user = request.user
    comments = Comment.objects.filter(advert_comment__author=user)
    f = CommentFilter(request.GET, queryset=comments)
    return render(request, 'my_comments.html', {'filter': f})


@login_required
def accept_comment(comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.accept()
    return redirect('/adverts/my_comments/')


@login_required
def delete_comment(comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/adverts/my_comments/')


class PostsView(ListView):
    model = Advert
    template_name = 'adverts.html'
    context_object_name = 'adverts'
    ordering = ['-creation_date']


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'create_comment.html'
    context_object_name = 'comment'
    form_class = CommentForm
    success_url = '/adverts/'


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'advert.html'
    context_object_name = 'advert'


class AddAdvertView(LoginRequiredMixin, CreateView):
    model = Advert
    template_name = 'add.html'
    context_object_name = 'add'
    form_class = AdvertForm
    success_url = '/adverts/'


class ChangeAdvertView(LoginRequiredMixin, UpdateView):
    template_name = 'add.html'
    form_class = AdvertForm
    success_url = '/adverts/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advert.objects.get(pk=id)
