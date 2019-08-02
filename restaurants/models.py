from datetime import timezone

from django.db import models


class Restaurant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.DateField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        ordering = ['day']
