from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index_page'), secure=True)
        self.assertEqual(response.status_code, 200)