from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from monApp.models import Categorie, Produit, Rayon, Statut


class HomeViewTest(TestCase):
    def test_home_without_param(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/home.html")
        self.assertIsNone(response.context["param"])
        self.assertContains(response, "Hello Django")

    def test_home_with_param(self):
        response = self.client.get(reverse("home", args=["CriCri"]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["param"], "CriCri")
        self.assertContains(response, "Hello CriCri")


class AboutViewTest(TestCase):
    def test_about_renders_about_template(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/about.html")
        self.assertContains(response, "Something about us")


class ContactViewTest(TestCase):
    def test_contact_renders_contact_template(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/contact.html")
        self.assertContains(response, "Contact us")


class ListProduitsViewTest(TestCase):
    def test_list_produits_renders_and_passes_products(self):
        produit = Produit.objects.create(
            intituleProd="Produit test",
            prixUnitaireProd=Decimal("10.00"),
            dateFabProd=date(2023, 1, 1),
        )

        response = self.client.get(reverse("produits"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/list_produits.html")
        self.assertEqual(list(response.context["produits"]), [produit])
        self.assertContains(response, "Produit test")


class ListCategoriesViewTest(TestCase):
    def test_list_categories_renders_and_passes_categories(self):
        categorie = Categorie.objects.create(nomCat="Catégorie test")

        response = self.client.get(reverse("categories"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/ListCategories.html")
        self.assertEqual(list(response.context["categoires"]), [categorie])
        self.assertContains(response, "Catégorie test")


class ListStatutsViewTest(TestCase):
    def test_list_statuts_renders_and_passes_statuses(self):
        statut = Statut.objects.create(libelleStatut="Statut test")

        response = self.client.get(reverse("statuts"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/ListStatuts.html")
        self.assertEqual(list(response.context["statuts"]), [statut])
        self.assertContains(response, "Statut test")


class ListRayonsViewTest(TestCase):
    def test_list_rayons_renders_and_passes_racks(self):
        rayon = Rayon.objects.create(nomRayon="Rayon test")

        response = self.client.get(reverse("rayons"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "monApp/ListRayons.html")
        self.assertEqual(list(response.context["rayons"]), [rayon])
        self.assertContains(response, "Rayon test")
