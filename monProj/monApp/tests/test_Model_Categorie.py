from datetime import date
from decimal import Decimal

from django.test import TestCase
from monApp.models import Categorie, Produit, Rayon, Statut


class CategorieModelTest(TestCase):
    def setUp(self):
        # Créer un attribut produit à utiliser dans les tests
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")

    def test_categorie_creation(self):
        self.assertEqual(self.ctgr.nomCat, "CategoriePourTest")

    def test_string_representation(self):
        self.assertEqual(str(self.ctgr), "CategoriePourTest")

    def test_categorie_updating(self):
        self.ctgr.nomCat = "CategoriePourTestsModifiee"
        self.ctgr.save()
        # Récupérer l'objet mis à jour
        updated_ctgr = Categorie.objects.get(idCat=self.ctgr.idCat)
        self.assertEqual(updated_ctgr.nomCat, "CategoriePourTestsModifiee")

    def test_categorie_deletion(self):
        self.ctgr.delete()
        self.assertEqual(Categorie.objects.count(), 0)


class StatusModelTest(TestCase):
    def setUp(self):
        self.statut = Statut.objects.create(libelle="En stock")

    def test_statut_creation(self):
        self.assertEqual(self.statut.libelle, "En stock")

    def test_string_representation_statut(self):
        self.assertEqual(str(self.statut), "En stock")

    def test_statut_updating(self):
        self.statut.libelle = "Plus en stock"
        self.statut.save()
        updated_statut = Statut.objects.get(idStatus=self.statut.idStatus)
        self.assertEqual(updated_statut.libelle, "Plus en stock")

    def test_statut_deletion(self):
        self.statut.delete()
        self.assertEqual(Statut.objects.count(), 0)


class RayonModelTest(TestCase):
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="Rayon Fruits")

    def test_rayon_creation(self):
        self.assertEqual(self.rayon.nomRayon, "Rayon Fruits")

    def test_string_representation_rayon(self):
        self.assertEqual(str(self.rayon), "Rayon Fruits")

    def test_rayon_updating(self):
        self.rayon.nomRayon = "Rayon Légumes"
        self.rayon.save()
        updated_rayon = Rayon.objects.get(idRayon=self.rayon.idRayon)
        self.assertEqual(updated_rayon.nomRayon, "Rayon Légumes")

    def test_rayon_deletion(self):
        self.rayon.delete()
        self.assertEqual(Rayon.objects.count(), 0)


class ProduitModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nomCat="Catégorie produit")
        self.statut = Statut.objects.create(libelle="Disponible")
        self.produit = Produit.objects.create(
            intituleProd="Produit test",
            prixUnitaireProd=Decimal("12.50"),
            dateFabrication=date(2024, 1, 15),
            categorie=self.categorie,
            statut=self.statut,
        )

    def test_produit_creation(self):
        self.assertEqual(self.produit.intituleProd, "Produit test")
        self.assertEqual(self.produit.prixUnitaireProd, Decimal("12.50"))
        self.assertEqual(self.produit.dateFabrication, date(2024, 1, 15))
        self.assertEqual(self.produit.categorie, self.categorie)
        self.assertEqual(self.produit.statut, self.statut)

    def test_string_representation_produit(self):
        self.assertEqual(str(self.produit), "Produit test")

    def test_produit_updating(self):
        self.produit.intituleProd = "Produit modifié"
        self.produit.prixUnitaireProd = Decimal("20.99")
        self.produit.save()
        updated_produit = Produit.objects.get(refProd=self.produit.refProd)
        self.assertEqual(updated_produit.intituleProd, "Produit modifié")
        self.assertEqual(updated_produit.prixUnitaireProd, Decimal("20.99"))

    def test_produit_deletion(self):
        self.produit.delete()
        self.assertEqual(Produit.objects.count(), 0)

