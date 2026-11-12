from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView
from .models import *

class HomeView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if 'param' in self.kwargs:
            context['param'] = self.kwargs['param']
        else:
            context['param'] = "Django"
        context['message'] = f"Hello {context['param']}"
        return context

class AboutView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['message'] = "Something about us"
        return context

class ContactView(TemplateView):
    template_name = "monApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['message'] = "Contact Django"
        return context

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


