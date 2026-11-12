from django.shortcuts import HttpResponse, render
from django.template import context
from django.views.generic import DetailView, ListView, TemplateView
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

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "produits"
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits !"
        return context
    
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    
def ListCategories(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/ListCategories.html',{'categoires': cats})

def ListStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/ListStatuts.html',{'statuts': stats})

def ListRayons(request):
    rays = Rayon.objects.all()
    return render(request, 'monApp/ListRayons.html',{'rayons': rays})


