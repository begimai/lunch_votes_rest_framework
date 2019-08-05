from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework_extensions.test import APITestCase

from restaurants.models import Restaurant
from restaurants.tests.helpers import EmployeeApiClientMixin


class TestCase(EmployeeApiClientMixin, APITestCase):
    def test_create_restaurant(self):
        url = reverse('api:restaurants-list')
        data = {'title': 'Bishkek'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().title, 'Bishkek')

    def test_delete_restaurant(self):
        restaurant = Restaurant.objects.create(title='Bishkek')
        url = reverse('api:restaurants-detail', args=[restaurant.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Restaurant.objects.count(), 0)
