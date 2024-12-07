from django.shortcuts import render
from django.views.generic import ListView, DetailView #Otra forma de importar todo es con *
from.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content','author']
    template_name = 'Post_New.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'post_update.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog-home')
