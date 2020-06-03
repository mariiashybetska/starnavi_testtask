from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # login/logout
    path('auth/', include('django.contrib.auth.urls')),

    # app
    path('sn/', include('social_network.urls')),

    # api
    path('api/', include('social_network.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# SWAGGER
schema_view = get_swagger_view(title='DOCS')
urlpatterns.append(path('api/docs/', schema_view))
