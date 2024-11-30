from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Post
from django.views.generic.edit import CreateView

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = ('post_detail.html')

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content','author']
    template_name = 'Post_New.html'
