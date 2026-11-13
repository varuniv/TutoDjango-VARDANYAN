from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import ContactUsForm
from .models import *


class HomeView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["param"] = self.kwargs.get("param")
        context["message"] = f"Hello {context['param'] or 'Django'}"
        return context


class AboutView(TemplateView):
    template_name = "monApp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Something about us"
        return context


def ContactView(request):
    message = "Contact us!"
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data["name"] or "anonyme"
            send_mail(
                subject=f"Message from {sender_name} via monProj Contact form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@monApp.com"],
            )
            return redirect("email-sent")
    else:
        form = ContactUsForm()

    return render(
        request,
        "monApp/home.html",
        {"message": message, "form": form},
    )


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


def EmailSentView(request):
    return render(request, "monApp/home.html", {"message": "Message envoyé"})