from django.urls import path

# My
from api.article import views 

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('detail/<int:pk>', views.ArticleDetailView.as_view(), name='detail_page'),
    path('edit-page', views.ArticleCreateView.as_view(), name='edit_page'),
    path('update-page/<int:pk>', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>', views.ArticleDeleteView.as_view(), name='delete_page'),
]   
