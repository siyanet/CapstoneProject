from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='index'),
    path("menu-Items/", views.MenuItemView.as_view(), name='menu'),
    path('menu-Items/<int:pk>/', views.SingleMenuItemView.as_view()),
    
    ]