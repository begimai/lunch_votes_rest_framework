import datetime

from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework_extensions.test import APITestCase

from restaurants.models import Menu, Restaurant
from restaurants.tests.helpers import RestaurantApiClientMixin

datetime.datetime.strptime('24052010', "%d%m%Y").date()


class MenuTestCase(RestaurantApiClientMixin, APITestCase):
    def setUp(self):
        super(MenuTestCase, self).setUp()

    def test_success(self):
        url = reverse('api:menu-list')
        data = {'title': 'menu #1', 'dishes': "multiple dishes"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.filter(restaurant__id=self.restaurant.id).count(), 1)
        self.assertEqual(Menu.objects.filter(restaurant__id=self.restaurant.id)[0].title, 'menu #1')

        # Getting result for all days, assuming that there is only one entry
        response = self.client.get(reverse('api:menu-result'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_menu(self):
        menu = Menu.objects.create(title='menu #1', restaurant=self.restaurant)
        url = reverse('api:menu-detail', args=[menu.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 0)

        # Getting result for all days, but there are no menu entries
        response = self.client.get(reverse('api:menu-result'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_result_multiple_menus(self):
        r1 = Restaurant.objects.create(title='Restaurant 1')
        r2 = Restaurant.objects.create(title='Restaurant 2')
        r3 = Restaurant.objects.create(title='Restaurant 3')
        Menu.objects.create(title='menu #1', date='2020-05-05', restaurant=r1)
        Menu.objects.create(title='menu #2', date='2019-05-05', restaurant=r2)
        Menu.objects.create(title='menu #3', date='2020-01-01', restaurant=r2)
        Menu.objects.create(title='menu #4', date='2010-01-01', restaurant=r3)

        self.assertEqual(Menu.objects.filter(restaurant__id=r1.id).count(), 1)
        self.assertEqual(Menu.objects.filter(restaurant__id=r2.id).count(), 2)
        self.assertEqual(Menu.objects.filter(restaurant__id=r3.id)[0].date, datetime.date(2010, 1, 1))
        self.assertEqual(Menu.objects.filter(restaurant__id=r1.id)[0].date, datetime.date(2020, 5, 5))
        self.assertEqual(Menu.objects.filter(restaurant__id=r1.id)[0].title, 'menu #1')
