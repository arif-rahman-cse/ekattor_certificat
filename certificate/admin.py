from django.contrib import admin

# Register your models here.
from certificate.models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', ]
    list_per_page = 50
    search_fields = ['name', 'id', ]
    ordering = ['created_at', ]

