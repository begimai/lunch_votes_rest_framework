from django.urls import path, include
from rest_framework.routers import DefaultRouter

from restaurants import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'dishes', views.DishViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
