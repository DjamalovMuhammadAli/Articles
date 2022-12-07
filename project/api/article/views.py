from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

# My
from article.models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from article.forms import ArticleForm


class ArticleListView(ListView):
  model = Article
  template_name = 'index.html'
  context_object_name = 'list_articles'


class ArticleDetailView(DetailView):
  model = Article
  template_name = 'detail.html'
  context_object_name = 'get_article'


class CustomSuccessMessageMixin:
  @property
  def success_msg(self):
    return False
  def form_valid(self, form):
    messages.success(self.request, self.success_msg)
    return super().form_valid(form)
  def get_success_url(self):
    return '%s?id=%s' % (self.success_url, self.object.id)


class ArticleCreateView(CustomSuccessMessageMixin, CreateView):
  model = Article
  template_name = 'edit_page.html'
  form_class = ArticleForm
  success_url = reverse_lazy('edit_page')
  success_msg = 'Notetion created'
  def get_context_data(self, **kwargs):
    kwargs['list_articles'] = Article.objects.all().order_by('-id')
    return super().get_context_data(**kwargs)


class ArticleUpdateView(CustomSuccessMessageMixin, UpdateView):
  model = Article
  template_name = 'edit_page.html'
  form_class = ArticleForm
  success_url = reverse_lazy('edit_page')
  success_msg = 'Notetion successful updated'
  def get_context_data(self, **kwargs):
    kwargs['update'] = True
    return super().get_context_data(**kwargs) 


class ArticleDeleteView(DeleteView):
  mode = Article
  template_name = 'edit_page.html'
  success_url = reverse_lazy('edit_page')
  success_msg = 'Notetion deleted'
  def post(self, request, *args, **kwargs):
    messages.success(self.request, self.success_msg)
    return super().post(request)













# def delete_page(request, pk):
#   get_article = Article.objects.get(pk=pk)
#   get_article.delete()
#   return redirect(reverse('edit_page'))


# def update_page(request, pk):

#   success_update = False

#   get_article = Article.objects.get(pk=pk)

#   if request.method == 'POST':
#     form = ArticleForm(request.POST, instance = get_article)
#     if form.is_valid():
#       form.save()
#       success_update = True
  
#   template = 'edit_page.html'
#   context = {
#     'get_article': get_article,
#     'update':True,
#     'form':ArticleForm(instance = get_article),
#     'success_update':success_update
#   }
#   return render(request, template, context)


# def edit_page(request):
#   success = False
#   if request.method == 'POST':
#     form = ArticleForm(request.POST)
#     if form.is_valid():
#       form.save()
#       success = True
#   template = 'edit_page.html'
#   context = {
#     'list_articles': Article.objects.all().order_by('-id'),
#     'form': ArticleForm(),
#     'success': success
#   }
#   return render(request, template, context)
