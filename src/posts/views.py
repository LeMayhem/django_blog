from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

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