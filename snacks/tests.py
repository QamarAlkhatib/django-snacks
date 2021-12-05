from django.test import SimpleTestCase
from django.urls import reverse


class SnacksTests(SimpleTestCase):
    def test_homepage_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_about_us_page_status_code(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_homepage_templates(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")
    def test_about_us_templates(self):
        url = reverse('about-us')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about-us.html")