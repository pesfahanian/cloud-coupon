from django.contrib.auth import get_user_model

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.serializers import (
    AuthTokenObtainPairSerializer,
    UserSerializer,
)

User = get_user_model()


class AuthTokenObtainPairAPIView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer


class UserGetAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    pagination_class = None

    queryset = User.active_objects.all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        instance = get_object_or_404(
            self.get_queryset(),
            id=self.request.user.id,
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
