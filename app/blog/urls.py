from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.detail, name='detail'),
    path('edit/<int:article_id>/', views.edit, name='edit'),
]
