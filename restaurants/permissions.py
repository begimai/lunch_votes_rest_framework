from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsRestaurantOrReadyOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or
            hasattr(request.user, 'restaurant')
        )