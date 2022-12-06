from django.urls import path

# My
from api.article import views 

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailDetailView.as_view(), name='detail_page'),
]
