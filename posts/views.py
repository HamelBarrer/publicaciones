from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm


class PostListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('-pk')


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    template_name = 'posts/add_post.html'
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('posts:post')


class PostDetailView(DetailView):
    template_name =
