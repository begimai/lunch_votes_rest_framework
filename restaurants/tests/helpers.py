from django.contrib.auth import get_user_model

from restaurants.models import Restaurant


class EmployeeApiClientMixin(object):
    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_superuser(username='test_user',
                                                  email='admin@example.com',
                                                  password='test_password')
        self.client.login(username='test_user', password='test_password')


class RestaurantApiClientMixin(object):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(title='test_restaurant')
        self.client.force_login(self.restaurant.user)
