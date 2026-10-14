from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView
from .models import *

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['message'] = "Hello Django!"
        return context

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


