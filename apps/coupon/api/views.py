from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.coupon.api.serializers import CouponSerializer
from apps.coupon.models import Coupon


class CouponListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CouponSerializer
    queryset = Coupon.enabled_objects.filter(count__gte=1)
