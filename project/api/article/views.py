from django.shortcuts import render

# My
from article.models import Article
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
  model = Article
  template_name = 'index.html'
  context_object_name = 'list_articles'


class DetailDetailView(DetailView):
  model = Article
  template_name = 'detail.html'
  context_object_name = 'get_article'


def edit_page(request):
  template = 'edit_page.html'
  context = {
    
  }
  return render(request, template, context)
