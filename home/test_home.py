from django.test import TestCase
from django.urls import reverse

class TestHomePage(TestCase):
    def test_homepage_status_code(self):
        url = reverse('home')  # 'home' URL name from home/urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
