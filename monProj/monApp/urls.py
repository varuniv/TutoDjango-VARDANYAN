from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("home/<param>", views.home, name="home"),    
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("listproduits", views.ListProduits, name="listproduits"),
    path("listcategories", views.ListCategories, name="listcategories"),
    path("liststatut", views.ListStatut, name="liststatut"),
    path("listrayons", views.ListRayons, name="listrayons"),
]