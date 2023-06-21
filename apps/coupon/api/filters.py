from django_filters import rest_framework as filters

from apps.coupon.models import CouponType, Server, UserCoupon


class UserCouponFilter(filters.FilterSet):
    type = filters.ChoiceFilter(
        field_name='coupon__type',
        choices=CouponType.choices,
    )
    server = filters.ChoiceFilter(
        field_name='coupon__server',
        choices=Server.choices,
    )
    is_used = filters.BooleanFilter(field_name='is_used')

    class Meta:
        model = UserCoupon
        fields = (
            'type',
            'server',
            'is_used',
        )
