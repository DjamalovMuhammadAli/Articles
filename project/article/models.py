from django.db import models


class Article(models.Model):
  created_date = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200)
  text = models.TextField()

  def __str__(self):
    return '%s:.%s-%s'%(self.created_date, self.name, self.text) 
