from rest_framework import serializers
from django.contrib.auth.models import User

from restaurants.models import Restaurant, Dish, Menu


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['url', 'id', 'name', 'description', 'address', 'phone_number', 'created']


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['url', 'id', 'name', 'description', 'price']


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    # restaurant = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    # dish = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = Menu
        fields = ['url', 'id', 'day', 'restaurant', 'dish']
