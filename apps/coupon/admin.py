from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from apps.core.admin import TemporalModelAdmin

from apps.coupon.models import Coupon, UserCoupon


@admin.register(Coupon)
class CouponAdmin(TemporalModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'code',
        'value',
        'type',
        'server',
        'count',
    ) + TemporalModelAdmin.list_display

    def get_readonly_fields(self, request: WSGIRequest, obj=None) -> tuple:
        if obj:
            return self.readonly_fields + (
                'code',
                'value',
                'type',
                'server',
            )
        return self.readonly_fields


@admin.register(UserCoupon)
class UserCouponAdmin(TemporalModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'user',
        'coupon',
        'is_used',
    ) + TemporalModelAdmin.list_display
