from django.contrib.auth import get_user_model
from django.db.models import Count, Q, F
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from restaurants.filters import MenuFilterSet
from restaurants.models import Restaurant, Menu, Vote
from restaurants.permissions import IsRestaurantOrReadyOnly
from restaurants.serializers import RestaurantSerializer, MenuSerializer, VoteSerializer, UserSerializer

User = get_user_model()


class RestaurantViewSet(ModelViewSet):
    model = Restaurant
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminUser]


class MenuViewSet(ModelViewSet):
    model = Menu
    queryset = Menu.objects.all().annotate(
        votes_for=Count('votes', filter=Q(votes__action=Vote.VOTE_FOR)),
        votes_against=Count('votes', filter=Q(votes__action=Vote.VOTE_AGAINST))
    )
    serializer_class = MenuSerializer
    permission_classes = [IsRestaurantOrReadyOnly]

    filterset_class = MenuFilterSet

    def perform_create(self, serializer):
        restaurant = self.request.user.restaurant
        serializer.save(restaurant=restaurant)

    @action(detail=False, methods=['GET'])
    def result(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        menu = qs.order_by('-votes_for').first()
        if menu is None:
            raise NotFound
        serializer = self.get_serializer(instance=menu)
        return Response(serializer.data)


class UserViewSet(ModelViewSet):
    model = User
    queryset = User.objects.all().filter(restaurant__isnull=True)
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class VoteViewSet(NestedViewSetMixin, ModelViewSet):
    model = Vote
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    # We assume that any user is that created
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        menu = Menu.objects.get(id=self.kwargs['parent_lookup_menu'])
        serializer.save(user=self.request.user, menu=menu)
