from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

auth_patterns = [
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]


urlpatterns = [
    path('auth/', include((auth_patterns, 'users'), namespace='auth')),
]
