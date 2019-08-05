from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token


schema_view = get_schema_view(
    openapi.Info(
        title='Restaurant API',
        default_version='v1',
        description='Restaurant API to select what employees want to get to',

    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_auth_token, name='token-auth'),
    path('api/', include('restaurants.urls', namespace='api')),
    path('docs/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
]