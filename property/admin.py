from django.contrib import admin

from property.models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address']
    readonly_fields = ['created_at']


admin.site.register(Flat, FlatAdmin)
