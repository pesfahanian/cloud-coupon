from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.wallet.api.serializers import WalletSerializer
from apps.wallet.models import Wallet


class WalletGetAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = WalletSerializer
    pagination_class = None

    queryset = Wallet.objects.all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        instance = get_object_or_404(
            self.get_queryset(),
            user__id=self.request.user.id,
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
