from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from . models import Post

class PostListView(ListView):
    model = Post
    template_name= 'post_list.html'


class PostCreateView(CreateView):
    model = Post
    Fields = "__all__"
    success_url = 'reverse_lazy("blog:all")'
    template_name = 'base.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__" 
    success_url = 'reverse_lazy("blog:all")'
    template_name = 'post_form.html'


class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__" 
    success_url = 'reverse_lazy("blog:all")'
    template_name = 'post_confirm_delete.html'







