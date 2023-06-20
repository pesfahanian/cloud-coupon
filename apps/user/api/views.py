from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.serializers import (
    AuthTokenObtainPairSerializer, )


class AuthTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer
