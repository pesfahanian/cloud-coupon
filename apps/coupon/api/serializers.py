from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.api.serializers import TemporalModelSerializer

from apps.coupon.handlers import user_coupon_create_handler
from apps.coupon.models import Coupon, UserCoupon

from apps.wallet.models import Wallet


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = (
            'id',
            'code',
            'value',
            'type',
            'server',
        )


class UserCouponListCreateSerializer(serializers.ModelSerializer):
    # ! Swagger UI schema is not shown correctly.
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    coupon = CouponSerializer(read_only=True)

    is_used = serializers.BooleanField(read_only=True)

    code = serializers.CharField(
        max_length=6,
        write_only=True,
        required=True,
    )

    class Meta:
        model = UserCoupon
        fields = (
            'id',
            'user',
            'code',
            'coupon',
            'is_used',
        ) + TemporalModelSerializer.Meta.fields

    def create(self, validated_data: dict) -> UserCoupon:
        user = validated_data['user']
        code = validated_data['code']

        try:
            user_coupon_obj = user_coupon_create_handler(
                user_id=user.id,
                code=code,
            )
            return user_coupon_obj

        except Exception as e:
            raise serializers.ValidationError(
                f'Failed to create user coupon. Reason: {str(e)}.')
