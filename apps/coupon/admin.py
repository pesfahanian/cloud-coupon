from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from apps.core.admin import TemporalModelAdmin, ToggleableModelAdmin

from apps.coupon.models import Coupon, UserCoupon


@admin.register(Coupon)
class CouponAdmin(TemporalModelAdmin, ToggleableModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'code',
        'value',
        'type',
        'server',
        'count',
        'selected_count',
        'used_count',
        'available_count',
    ) + TemporalModelAdmin.list_display + ToggleableModelAdmin.list_display

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
class UserCouponAdmin(TemporalModelAdmin, ToggleableModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'user',
        'coupon',
        'is_used',
    ) + TemporalModelAdmin.list_display + ToggleableModelAdmin.list_display
