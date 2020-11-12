from django.contrib import admin

from property.models import Claim, Flat, Owner


class ClaimAdmin(admin.ModelAdmin):
    """Отображение жалобы в админке."""

    raw_id_fields = ('owner', 'flat')
    list_display = ['owner', 'flat', 'text']


class OwnerInline(admin.TabularInline):
    model = Owner.flat_owner.through
    extra = 0


class FlatAdmin(admin.ModelAdmin):
    """Отображение квартир в админке."""

    search_fields = ['town', 'address', 'pk']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('like', )
    list_per_page = 20
    # TODO очень медленное открытие объекта
    # inlines = [OwnerInline]


class OwnerAdmin(admin.ModelAdmin):
    """Отображение собственников квартиры."""

    list_display = ['owner', 'owner_pure_phone']
    raw_id_fields = ('flat_owner', )
    search_fields = ['owner', 'owner_pure_phone']
    list_per_page = 20
    # TODO очень медленное открытие объекта
    # inlines = [OwnerInline]
    # exclude = ('flat_owner', )


admin.site.register(Claim, ClaimAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
