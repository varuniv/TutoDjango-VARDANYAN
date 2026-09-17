from django.test import TestCase
from django.urls import reverse

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
