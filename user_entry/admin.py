from django.contrib import admin

# Register your models here.
from user_entry.models import UserEntry


@admin.register(UserEntry)
class UserEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_en', 'nid_no', 'present_area_village_en', 'date_of_birth', ]
    list_per_page = 50
    search_fields = ['name_en', 'id', ]
    ordering = ['created_at', ]
