from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article

# Class based articles list view
class ArticleListView(ListView):
    queryset = Article.published.all()
    length = len(queryset)
    context_object_name = 'articles'
    paginate_num = 3
    paginate_by = paginate_num
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['length'] = self.length
        context['paginate_num'] = self.paginate_num
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'website/detail.html'
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

