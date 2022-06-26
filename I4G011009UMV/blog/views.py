from msilib.schema import ListView, CreateView, UpdateView, DetailView
from typing import List
from django.shortcuts import render
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post 
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post 
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post 
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

