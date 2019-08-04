from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurants import views

# Create a router and register our viewsets with it.
from restaurants.views import UserViewSet, MenuViewSet, RestaurantViewSet, VoteViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

restaurant_router = router.register('restaurants', RestaurantViewSet, basename='restaurants')

menu_router = router.register('menu', MenuViewSet,
                              basename='menu')

menu_router.register('votes', VoteViewSet,
                     basename='menu-votes',
                     parents_query_lookups=['menu__restaurant', 'menu'])

app_name = 'restaurants'
urlpatterns = [

]

urlpatterns += router.urls