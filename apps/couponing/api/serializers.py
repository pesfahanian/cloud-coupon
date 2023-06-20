from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.api.serializers import TemporalModelSerializer

from apps.couponing.models import Coupon, UserCoupon


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = (
            'id',
            'code',
            'value',
            'server',
            'created_at',
        )
