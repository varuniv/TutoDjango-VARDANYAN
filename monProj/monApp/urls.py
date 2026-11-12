from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path("home/", views.home, name="home"),
    path('home/<param>', views.HomeView.as_view(), name='home'),
    path("", views.HomeView.as_view(), name="home"),
    path("home", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path('produits/', views.ProduitListView.as_view(), name='produits'),
    path('categories/',views.ListCategories ,name='categories'),
    path('statuts/',views.ListStatuts,name='statuts'),
    path('rayons/',views.ListRayons,name='rayons'),
    path("produit/<pk>/",views.ProduitDetailView.as_view()),
    
]