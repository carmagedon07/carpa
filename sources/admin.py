from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from main.admin import BaseModelAdmin
from sources.models import Parcel, ParcelOwner


@admin.register(ParcelOwner)
class ParcelOwnerAdmin(admin.ModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': BaseModelAdmin.readonly_fields
        }),
        ('Person', {
            'fields': (('first_name', 'last_name',),)
        }),
        ('Address', {
            'fields': ('organization', 'address_1', 'address_2',)
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'website',)
        })
    )
    list_display = ('id', 'first_name', 'last_name', 'email',)
    list_filter = ('creation_date',)


@admin.register(Parcel)
class ParcelAdmin(gis_admin.OSMGeoAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields
    fieldsets = (
        (None, {
            'fields': (BaseModelAdmin.readonly_fields + ('is_active',),)
        }),
        ('Parcel information', {
            'fields': ('name', 'owner',),
        }),
        ('Physical information', {
            'fields': ('location', 'extension',),
        })
    )
    list_display = ('id', 'name', 'owner', 'extension',)
    list_filter = ('creation_date',)
    default_lat = 454018.69011
    default_lon = -8191521.69263
    default_zoom = 15