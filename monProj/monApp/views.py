from django.shortcuts import HttpResponse
from .models import *

def home(request,param=""):
    return HttpResponse("<h1>Bonjour " + param + " !</h1>")

def contactus(request):
    return HttpResponse("<h1>Contact Us</h1>")

def aboutus(request):
    return HttpResponse("<h1>Something about us</h1>")

def ListProduits(request):
    prdts = Produit.objects.all()
    html = "<h1>Liste des produits</h1>"
    for prdt in prdts:
        html += "<li>" + prdt.intituleProd + "</li>"
    return HttpResponse(html)

def ListCategories(request):
    cats = Categorie.objects.all()
    html = "<h1>Liste des catégories</h1>"
    for cat in cats:
        html += "<li>" + cat.nomCat + "</li>"
    return HttpResponse(html)

def ListStatut(request):
    stats = Statut.objects.all()
    html = "<h1>Liste des statuts</h1>"
    for stat in stats:
        html += "<li>" + stat.libelleStatut + "</li>"
    return HttpResponse(html)

def ListRayons(request):
    rays = Rayon.objects.all()
    html = "<h1>Liste des rayons</h1>"
    for ray in rays:
        html += "<li>" + ray.nomRayon + "</li>"
    return HttpResponse(html)
