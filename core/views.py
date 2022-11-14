from django.shortcuts import render

from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
)
from .models import Article, Category, Image
from .forms import CategoryCreateForm, ImageCreateForm, ArticleCreateForm

# Create your views here.

class ArticleListView(ListView):
    template_name = "index.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        
        return context
