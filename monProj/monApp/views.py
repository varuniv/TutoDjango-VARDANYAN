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
    
class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/ListCategories.html"
    context_object_name = "categories"
    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories !"
        return context
    
class StatutListView(ListView):
    model = Statut
    template_name = "monApp/ListStatuts.html"
    context_object_name = "statuts"
    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes statuts !"
        return context

class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/ListRayons.html"
    context_object_name = "rayons"
    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons !"
        return context


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categories.html"
    context_object_name = "categories"
    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context

class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "statuts"
    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context

class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayons.html"
    context_object_name = "rayons"
    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context