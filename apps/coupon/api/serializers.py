from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.api.serializers import TemporalModelSerializer

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


class UserCouponListSerializer(TemporalModelSerializer):
    coupon = CouponSerializer(read_only=True)

    class Meta:
        model = UserCoupon
        fields = (
            'id',
            'coupon',
            'is_used',
        ) + TemporalModelSerializer.Meta.fields


class UserCouponCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
        )

    def create(self, validated_data: dict) -> UserCoupon:
        user = validated_data['user']
        code = validated_data['code']

        user_id = user.id

        try:
            wallet_obj = Wallet.objects.get(user_id=user_id)
        except Wallet.DoesNotExist:
            raise serializers.ValidationError(
                'Wallet for this user does not exist.')

        try:
            coupon_obj = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            raise serializers.ValidationError('Invalid coupon.')

        user_coupon_obj = UserCoupon.objects.create(
            user_id=user_id,
            coupon=coupon_obj,
        )

        return user_coupon_obj
