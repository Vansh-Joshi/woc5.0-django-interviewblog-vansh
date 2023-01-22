from django.urls import path
from . import views

urlpatterns =[

    path('', views.home),
    path('bijubadhu/', views.bijubadhu),
    path('Profile/', views.profile),
    path('Explore/', views.explore),
    path('Myexperiences/', views.myexperiences),
    path('Bookmarks/', views.bookmarks),
    path('login/', views.login),
    path('register/', views.register),


]
