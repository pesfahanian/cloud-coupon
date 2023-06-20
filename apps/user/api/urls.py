from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.api.views import (
    AuthTokenObtainPairAPIView, )

urlpatterns = [
    path(
        'login',
        AuthTokenObtainPairAPIView.as_view(),
        name='login',
    ),
    path(
        'token',
        TokenRefreshView.as_view(),
        name='token',
    ),
]
