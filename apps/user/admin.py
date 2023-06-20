from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'created_at',
        'updated_at',
        'last_login',
        'is_active',
    )
    search_fields = (
        'id',
        'username',
        'email',
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
        'last_login',
    )
