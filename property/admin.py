from django.contrib import admin

from property.models import Claim, Flat, Owner


class ClaimAdmin(admin.ModelAdmin):
    """Отображение жалобы в админке."""

    raw_id_fields = ('owner', 'flat')
    list_display = ['owner', 'flat', 'text']


class FlatAdmin(admin.ModelAdmin):
    """Отображение квартир в админке."""

    search_fields = ['owner', 'town', 'address', 'pk']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('like', )


class OwnerAdmin(admin.ModelAdmin):
    """Отображение собственников квартиры."""

    raw_id_fields = ('flat_owner', )


admin.site.register(Claim, ClaimAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
