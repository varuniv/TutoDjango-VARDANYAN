from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    #path("", views.home, name="home"),
    #path("home/", views.home, name="home"),
    #path('home/<param>',views.home ,name='home'),    
    #path('home/<param>',views.home ,name='home'),
    path("home", TemplateView.as_view(template_name="monApp/home.html")),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('produits/',views.ListProduits ,name='produits'),
    path('categories/',views.ListCategories ,name='categories'),
    path('statuts/',views.ListStatuts,name='statuts'),
    path('rayons/',views.ListRayons,name='rayons'),
    
]