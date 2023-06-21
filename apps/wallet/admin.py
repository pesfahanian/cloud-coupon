from django.contrib import admin

from apps.core.admin import TemporalModelAdmin

from apps.wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(TemporalModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'user',
        'balance',
    ) + TemporalModelAdmin.list_display
