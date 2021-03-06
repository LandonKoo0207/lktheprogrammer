from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Post, Category

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

class CategoryListView(ListView):
    template_name='blog/post_create.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

class PostListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

class PostDetailView(DetailView):
    template_name='blog/blog_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    fields = ['title', 'contents', 'category']

    template_name_suffix = '_create'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Post
    fields = ['title', 'contents', 'category']

    template_name_suffix = '_update'

def PostDeleteView(request, id):
    post_to_delete = get_object_or_404(Post, pk=id).delete()

    return HttpResponseRedirect('/')
