from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service

# Register your models here.


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Service model.

    Defines list display fields, Summernote editor fields,
    and default ordering for the admin interface.
    """
    list_display = (
        'service_type',
        'name',
        'duration',
        'price',
        'session_count'
    )

    summernote_fields = ('description',)

    ordering = ['service_type']
