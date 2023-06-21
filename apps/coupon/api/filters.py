from django_filters import rest_framework as filters

from apps.coupon.models import Coupon, CouponType, Server


class CouponFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=CouponType.choices)
    server = filters.ChoiceFilter(choices=Server.choices)

    class Meta:
        model = Coupon
        fields = ()
