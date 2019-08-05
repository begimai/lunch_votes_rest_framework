from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework_extensions.test import APITestCase

from restaurants.models import Restaurant, Menu, Vote, User
from restaurants.tests.helpers import EmployeeApiClientMixin


class MenuVoteTestCase(EmployeeApiClientMixin, APITestCase):
    def setUp(self):
        super(MenuVoteTestCase, self).setUp()
        self.restaurant = Restaurant.objects.create(title='bishkek')
        self.user = User.objects.create(username='bishkek')
        self.menu = Menu.objects.create(title='menu #1', restaurant=self.restaurant)

    def test_create_vote(self):
        url = reverse('api:menu-votes-list', args=[self.menu.id])
        data = {'action': 0, 'menu': self.menu.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.filter(menu__id=self.menu.id).count(), 1)
