from django.urls import path

# My
from api.article import views 

urlpatterns = [
    # path('articles/', views.articles),
    path('', views.ArticleListView.as_view()),
    path('detail/<int:id>', views.detail)
]
