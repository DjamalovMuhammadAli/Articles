from django.urls import path

# My
from api.article import views 

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailDetailView.as_view(), name='detail_page'),
    path('edit-page', views.edit_page, name='edit_page'),
    path('update-page/<int:pk>', views.update_page, name='update_page'),
    path('delete-page/<int:pk>', views.delete_page, name='delete_page'),
]   
