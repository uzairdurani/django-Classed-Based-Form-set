
from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='authors_create'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
  
]
