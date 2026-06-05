from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(LoginRequiredMixin, CreateView):  # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(LoginRequiredMixin, UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
