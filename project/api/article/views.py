from django.shortcuts import render

# My
from article.models import Article
from django.views.generic import ListView, DetailView
from article.forms import ArticleForm


class ArticleListView(ListView):
  model = Article
  template_name = 'index.html'
  context_object_name = 'list_articles'


class DetailDetailView(DetailView):
  model = Article
  template_name = 'detail.html'
  context_object_name = 'get_article'


def edit_page(request):
  success = False
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      form.save()
      success = True

  template = 'edit_page.html'
  context = {
    'list_articles': Article.objects.all().order_by('-id'),
    'form': ArticleForm(),
    'success': success
  }
  return render(request, template, context)

def update_page(request, pk):

  success_update = False

  get_article = Article.objects.get(pk=pk)

  if request.method == 'POST':
    form = ArticleForm(request.POST, instance = get_article)
    if form.is_valid():
      form.save()
      success_update = True
  
  template = 'edit_page.html'
  context = {
    'get_article': get_article,
    'update':True,
    'form':ArticleForm(instance = get_article),
    'success_update':success_update
  }

  return render(request, template, context)
