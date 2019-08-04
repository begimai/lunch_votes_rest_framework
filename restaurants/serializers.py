from rest_framework import serializers
from django.contrib.auth.models import User

from restaurants.models import Restaurant, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'title',
            'token',
        ]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={
        'input_type': 'password',
    })

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]


class MenuSerializer(serializers.ModelSerializer):
    votes_for = serializers.IntegerField(read_only=True)
    votes_against = serializers.IntegerField(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'id',
            'title',
            'date',
            'restaurant',
            'votes_for',
            'votes_against',
            'dishes',
        ]


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    menu = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = [
            'id',
            'user',
            'menu',
            'action',
        ]

    def create(self, validated_data):
        Vote.objects.filter(user=validated_data['user'], menu=validated_data['menu']).delete()
        return super(VoteSerializer, self).create(validated_data)