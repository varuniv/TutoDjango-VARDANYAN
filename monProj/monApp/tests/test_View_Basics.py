from django.test import TestCase
from django.urls import reverse
from monApp.models import Produit, Categorie, Statut, Rayon

class HomeViewTest(TestCase):

    # test de l'url de la page d'accueil
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    # test du contenu de la page d'accueil
    def test_home_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Bonjour  !</h1>')
        response = self.client.get(reverse('home', args=['CriCri']))
        self.assertContains(response, '<h1>Bonjour CriCri !</h1>')

class ContactUsViewTest(TestCase):
    # test de l'url de la page contact us
    def test_contactus_status_code(self):
        response = self.client.get(reverse('contactus'))
        self.assertEqual(response.status_code, 200)
    # test du contenu de la page contact us
    def test_contactus_content(self):
        response = self.client.get(reverse('contactus'))
        self.assertContains(response, '<h1>Contact Us</h1>')

class AboutUsViewTest(TestCase):
    # test de l'url de la page about us
    def test_aboutus_status_code(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
    # test du contenu de la page about us
    def test_aboutus_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, '<h1>Something about us</h1>')

class ListProduitsViewTest(TestCase):
    def setUp(self):
        self.produit = Produit.objects.create(intituleProd="ProduitTest", prixUnitaireProd=10.0, dateFabProd="2023-01-01")

    def test_listproduits_status_code(self):
        response = self.client.get(reverse('listproduits'))
        self.assertEqual(response.status_code, 200)

    def test_listproduits_content(self):
        response = self.client.get(reverse('listproduits'))
        self.assertContains(response, '<h1>Liste des produits</h1>')
        self.assertContains(response, f"<li>{self.produit.intituleProd}</li>")


class ListCategoriesViewTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nomCat="CategoriePourTests")

    def test_listcategories_status_code(self):
        response = self.client.get(reverse('listcategories'))
        self.assertEqual(response.status_code, 200)
            
    def test_listcategories_content(self):
        response = self.client.get(reverse('listcategories'))
        self.assertContains(response, '<h1>Liste des catégories</h1>')
        self.assertContains(response, f"<li>{self.categorie.nomCat}</li>")

class ListStatutViewTest(TestCase):
    def setUp(self):
        self.statut = Statut.objects.create(libelleStatut="StatutPourTests")

    def test_liststatut_status_code(self):
        response = self.client.get(reverse('liststatut'))
        self.assertEqual(response.status_code, 200)

    def test_liststatut_content(self):
        response = self.client.get(reverse('liststatut'))
        self.assertContains(response, '<h1>Liste des statuts</h1>')
        self.assertContains(response, f"<li>{self.statut.libelleStatut}</li>")

class ListRayonsViewTest(TestCase):
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTests")

    def test_listrayons_status_code(self):
        response = self.client.get(reverse('listrayons'))
        self.assertEqual(response.status_code, 200)

    def test_listrayons_content(self):
        response = self.client.get(reverse('listrayons'))
        self.assertContains(response, '<h1>Liste des rayons</h1>')
        self.assertContains(response, f"<li>{self.rayon.nomRayon}</li>")