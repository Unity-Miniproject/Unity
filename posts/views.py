from django.contrib.auth.models import Permission
from django.http.response import Http404
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailedView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [ 'question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostAnswerView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    
    fields = ['answer1']
    try :
        def form_valid(self, form):
            form.instance.author != self.request.user
            return super().form_valid(form)

        def test_func(self):
            post = self.get_object()
            if self.request.user != post.author:
                return True
            return False
    except PermissionError:
        raise Http404("Permission denied")
