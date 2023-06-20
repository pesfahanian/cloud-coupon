from django.contrib import admin
from django.db import models


class ToggleableModelAdmin(admin.ModelAdmin):
    list_display = ('is_enabled', )


class TemporalModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    list_display = (
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at', )
