from django.conf.urls import url
from .views import ArticleListView, ArticleDetailView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^about$', TemplateView.as_view(template_name='website/about.html'), name='about'),
    url(r'^contact$', TemplateView.as_view(template_name='website/contact.html'), name='contact'),
    url(r'^resume$', TemplateView.as_view(template_name='website/resume.html'), name='resume'),
    url(r'^reviews$', TemplateView.as_view(template_name='website/reviews.html'), name='reviews'),
    url(r'^tutorials$', TemplateView.as_view(template_name='website/tutorials.html'), name='tutorials'),
    url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail')
]