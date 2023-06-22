from django_filters import rest_framework as filters

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.coupon.api.filters import UserCouponFilter
from apps.coupon.api.serializers import UserCouponListCreateSerializer
from apps.coupon.models import UserCoupon


class UserCouponListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserCouponListCreateSerializer

    queryset = UserCoupon.objects.all()

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = UserCouponFilter

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).\
            filter(user__id=self.request.user.id, )
