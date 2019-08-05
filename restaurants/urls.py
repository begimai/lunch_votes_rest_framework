from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from restaurants.views import RestaurantViewSet, MenuViewSet, VoteViewSet, UserViewSet

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
