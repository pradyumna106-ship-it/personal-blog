from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_article, name='add-article'),
    path('edit/<int:pk>/', views.edit_article, name='edit-article'),
]
