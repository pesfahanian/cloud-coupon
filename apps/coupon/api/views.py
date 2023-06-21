from django_filters import rest_framework as filters

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.coupon.api.filters import CouponFilter
from apps.coupon.api.serializers import CouponSerializer
from apps.coupon.models import Coupon


class CouponListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CouponSerializer
    queryset = Coupon.enabled_objects.filter(count__gte=1)

    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CouponFilter
