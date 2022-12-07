from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# My
from .models import Article


class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control'


class AuthUserForm(AuthenticationForm, forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'password')
    def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'
