from django.contrib import admin

# Register your models here.
from GeoCodeBD.models import Division, District, Upazila, Union


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_bn', 'url', ]
    list_per_page = 50
    search_fields = ['name', 'id', ]
    ordering = ['created_at', ]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_bn', 'url', ]
    list_per_page = 50
    search_fields = ['name', 'id', ]
    ordering = ['created_at', ]


@admin.register(Upazila)
class UpazilaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_bn', 'url', ]
    list_per_page = 50
    search_fields = ['name', 'id', ]
    ordering = ['created_at', ]


@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_bn', 'url', ]
    list_per_page = 50
    search_fields = ['name', 'id', ]
    ordering = ['created_at', ]
