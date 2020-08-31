from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Panel, name="panel"),
    path('news_list/', views.News_List, name="news_list"),
    path('add_news/', views.Add_News, name="add_news"),
    path('login/', views.Login, name="login"),
    path('register/', views.Register, name="register"),
    path('logout/', views.Logout, name="logout_site"),
    path('news/publish/<int:pk>', views.News_Publish, name="news_publish"),
]
