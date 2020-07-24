from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import (
    Post,
    Commentary,
)
from .forms import (
    PostForm,
    CommentaryForm,
)

from profiles.models import Profile


class PostListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quantity'] = Commentary.objects.all().count()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    template_name = 'posts/add_post.html'
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('posts:post')


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    template_name = 'posts/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentary'] = Commentary.objects.all().order_by('-pk')
        return context


@login_required(login_url='users:login')
def create_commentary(request):
    template_name = 'posts/snippets/commentary.html'
    form = CommentaryForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        commentaries = request.POST.get('commentary')
        commentary = form.save(commit=False)
        commentary.user = request.user
        commentary.commentary = commentaries
        commentary.save()
        return redirect('posts:post')

    return render(request, template_name, {
        'form': form,
    })
