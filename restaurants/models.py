import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F
from rest_framework.authtoken.models import Token

User = get_user_model()


class RestaurantManager(models.Manager):
    def get_queryset(self):
        qs = super(RestaurantManager, self).get_queryset()
        qs = qs.annotate(token=F('user__auth_token__key'))
        return qs


class Restaurant(models.Model):
    title = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant', null=True)
    # address, geolocation, banner can be added later

    objects = RestaurantManager()

    def save(self, *args, **kwargs):
        if self.user is None:
            user = User.objects.create_user("{}_user".format(self.title))
            Token.objects.create(user=user)
            self.user = user
        super(Restaurant, self).save(*args, **kwargs)


class Menu(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', related_name='menu', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    approved = models.BooleanField(default=False)
    dishes = models.TextField()


class Vote(models.Model):
    """
    can be replaced with django-vote
    """
    VOTE_FOR = 0
    VOTE_AGAINST = 1
    VOTE_CHOICES = [
        (VOTE_FOR, '+'),
        (VOTE_AGAINST, '-')
    ]
    menu = models.ForeignKey('restaurants.Menu', related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    action = models.SmallIntegerField(choices=VOTE_CHOICES)
    created = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        unique_together = ['user', 'menu']
