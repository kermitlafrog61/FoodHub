import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f'Product {n}')
    ingredients = 'Lettuce, Tomato, Cucumber'
    price = 10.00
    photo = None
    popularity = 0
    type = 'salad'


class ProductViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product1 = ProductFactory(
            name='Salad 1', popularity=5, type='salad', price=12.00)
        self.product2 = ProductFactory(
            name='Salad 2', popularity=10, type='salad', price=8.00)
        self.product3 = ProductFactory(
            name='Soup 1', popularity=2, type='soup', price=15.00)
        self.product4 = ProductFactory(
            name='Soup 2', popularity=7, type='soup', price=10.00)

    def test_list_products(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_filter_products_by_type(self):
        response = self.client.get(reverse('product-list'), {'type': 'salad'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_products_by_popularity(self):
        response = self.client.get(
            reverse('product-list'), {'ordering': '-popularity'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Salad 2')

    def test_order_products_by_novelty(self):
        response = self.client.get(
            reverse('product-list'), {'ordering': '-novelty'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Soup 2')

    def test_order_products_by_price(self):
        response = self.client.get(
            reverse('product-list'), {'ordering': 'price'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Salad 2')

    def test_retrieve_product_and_increment_popularity(self):
        response = self.client.get(
            reverse('product-detail', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.popularity, 6)
