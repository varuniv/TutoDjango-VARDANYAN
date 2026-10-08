from django.shortcuts import HttpResponse, render
from .models import *

def home(request, param=None):
    return render(request, 'monApp/home.html', {'param':param})

def about(request):
    return render(request, 'monApp/about.html')

def contact(request):
    return render(request, 'monApp/contact.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'produits': prdts})

def ListCategories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/ListCategories.html',{'categoires': cats})

def ListStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/ListStatuts.html',{'statuts': stats})

def ListRayons(request):
    rays = Rayon.objects.all()
    return render(request, 'monApp/ListRayons.html',{'rayons': rays})


