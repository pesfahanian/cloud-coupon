from django.contrib import admin

from apps.core.admin import TemporalModelAdmin, ToggleableModelAdmin

from apps.wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(TemporalModelAdmin, ToggleableModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'user',
        'balance',
    ) + TemporalModelAdmin.list_display + ToggleableModelAdmin.list_display
