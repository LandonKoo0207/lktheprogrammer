from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Post, Category

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'blog/about.html')

class CategoryListView(ListView):
    template_name='blog/post_create.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

class PostListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

@login_required
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'contents', 'category']

    template_name_suffix = '_create'

@login_required
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'contents', 'category']

    template_name_suffix = '_update'

@login_required
def PostDeleteView(request, id):
    post_to_delete = get_object_or_404(Post, pk=id).delete()

    return HttpResponseRedirect('/blog')
