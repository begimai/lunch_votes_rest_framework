from rest_framework import viewsets, renderers
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from restaurants.models import Restaurant, Dish, Menu
from restaurants.serializers import UserSerializer, RestaurantSerializer, DishSerializer, MenuSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        restaurant = self.get_object()
        return Response(restaurant.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class DishViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        dish = self.get_object()
        return Response(dish.highlighted)

    def perform_create(self, serializer):
        serializer.save()


class MenuViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        menu = self.get_object()
        return Response(menu.highlighted)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })