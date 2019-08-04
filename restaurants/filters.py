from django_filters import FilterSet

from restaurants.models import Menu


class MenuFilterSet(FilterSet):
    class Meta:
        model = Menu
        fields = ['date']