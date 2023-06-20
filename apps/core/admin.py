from django.contrib import admin


def custom_titled_filter(title: str) -> admin.FieldListFilter:

    class Wrapper(admin.FieldListFilter):

        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


class ReadOnlyInlineAdminMixin:

    def has_add_permission(self, *args, **kwargs) -> bool:
        return False

    def has_change_permission(self, *args, **kwargs) -> bool:
        return False

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False


class TemporalModelReadOnlyFieldsMixin:
    readonly_fields = (
        'createdAt',
        'updatedAt',
    )


class TemporalModelInlineAdminMixin(TemporalModelReadOnlyFieldsMixin):
    extra = 0
    show_change_link = True


class TemporalModelTabularInlineAdmin(TemporalModelInlineAdminMixin,
                                      admin.TabularInline):
    pass


class TemporalModelStackedInlineAdmin(TemporalModelInlineAdminMixin,
                                      admin.StackedInline):
    pass


class ToggleableModelAdmin(admin.ModelAdmin):
    list_display = ('isEnabled', )
    list_filter = ('isEnabled', )


class TemporalModelAdmin(TemporalModelReadOnlyFieldsMixin, admin.ModelAdmin):
    pass
