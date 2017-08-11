from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Article
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Article.objects.all(),
                                template_name="news_home.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Article,
                                             template_name="news_article.html")),
    url(r'^header/', views.header, name='header'),
    url(r'^update/', views.update, name='update')
]
