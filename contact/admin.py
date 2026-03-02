from django.contrib import admin
from .models import ContactMessage, CompanyDetails


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'full_name', 'email', 'date', 'read')
    list_filter = ('date', 'read',)
    search_fields = ('full_name', 'email')
    fields = (
        'full_name', 'subject', 'email', 'phone_number',
        'message', 'read', 'date'
    )
    readonly_fields = ('date',)


@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'updated_on',)
