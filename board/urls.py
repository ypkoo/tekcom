from django.urls import path
from board import views

urlpatterns = [
    path('new/', views.index, name='index'),
    path('articles/', views.ArticleList.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
]