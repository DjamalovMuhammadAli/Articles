from django.shortcuts import render

# My
from article.models import Article
from django.views.generic import ListView, DetailView

# def get_article(request):
#   list_articles = Article.objects.all()
#   context = {
#     'name': 'Ali',
#     'text': list_articles,
#   }
#   template = 'articles.html'
#   return render(request, template, context)


class ArticleListView(ListView):
  model = Article
  template_name = 'articles.html'
  context_object_name = 'list_articles'


# def get_details(request, id):
#   get_articles = Article.objects.get(id=id)
#   context = {
#     'get_articles': get_articles,
#   }
#   template = 'detail.html'
#   return render(request, template, context)


class DetailDetailView(DetailView):
  model = Article
  template_name = 'detail.html'
  context_object_name = 'get_article'
