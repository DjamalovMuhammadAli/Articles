from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# My
from .middleware import get_current_user


class Article(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner of article', blank=True, null=True)
  created_date = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200)
  text = models.TextField()

  def __str__(self):
    return self.name 
    # return '%s: %s-%s'%(self.created_date, self.name, self.text) 


class StatusFilterComments(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(Q(status=False, author = get_current_user()) | Q(status=False, article__author=get_current_user()) | Q(status=True))
    

class Comments(models.Model):
  article = models.ForeignKey(Article, on_delete = models.CASCADE, blank = True, null = True, related_name='comments_articles' )
  author = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True )
  create_date = models.DateTimeField(auto_now=True)
  text = models.TextField()
  status = models.BooleanField(default=False) 
  objects  = StatusFilterComments()
