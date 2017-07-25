from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Class based articles list view
class ArticleListView(ListView):
    queryset = Article.published.all()
    context_object_name = 'articles'
    paginate_by = 10
    template_name = 'website/index.html'

