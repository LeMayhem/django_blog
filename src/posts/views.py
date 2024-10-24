from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from posts.models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()

        #Si user connecté, on retourne l'ensemble du queryset, sinon on n'affiche que les articles publiés
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)
    
#Vue de création d'article
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content',]

#Vue d'update d'article
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', "published"]

#Vue d'update d'article
class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "posts/blogpost_detail.html"
    context_object_name = "post"

#Vue d'update d'article
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")