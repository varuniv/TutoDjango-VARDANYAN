from django.urls import path

from . import views

urlpatterns = [
    #path("home/", views.home, name="home"),
    path('home/<param>', views.HomeView.as_view(), name='home'),
    path("", views.HomeView.as_view(), name="home"),
    path("home", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("produits/",views.ProduitListView.as_view(),name="listProduits"),
    path('categories/',views.CategorieListView.as_view(),name='categories'),
    path('statuts/',views.StatutListView.as_view(),name='statuts'),
    path('rayons/',views.RayonListView.as_view(),name='rayons'),
    path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="detailProduit"),
    path("categorie/<pk>/" ,views.CategorieDetailView.as_view(), name="detailCategorie"),
    path("statut/<pk>/" ,views.StatutDetailView.as_view(), name="detailStatut"),
    path("rayon/<pk>/" ,views.RayonDetailView.as_view(), name="detailRayon"),
    path("contact/", views.ContactView, name="contact"),
    path("email-sent/", views.EmailSentView, name="email-sent"),
]