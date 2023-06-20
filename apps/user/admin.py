from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.core.admin import TemporalModelAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id', ) + TemporalModelAdmin.readonly_fields
    list_display = (
        'username',
        'is_active',
        'last_login',
    ) + TemporalModelAdmin.list_display
    search_fields = (
        'id',
        'username',
    )
    list_filter = (
        'is_active',
        'last_login',
    ) + TemporalModelAdmin.list_filter
