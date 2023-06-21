from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.api.serializers import TemporalModelSerializer

from apps.coupon.models import Coupon, UserCoupon


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = (
            'id',
            'code',
            'count',
            'value',
            'type',
            'server',
            'created_at',
        )
