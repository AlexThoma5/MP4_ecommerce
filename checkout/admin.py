from django.contrib import admin
from .models import Order, OrderLineItem, Discount


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin configuration for OrderLineItem.

    Displays line items within the Order admin and marks
    'lineitem_total' as read-only.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.

    Includes OrderLineItem inlines, sets read-only fields,
    defines which fields are displayed and the ordering
    in the admin list view.
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number', 'date', 'order_total',
        'grand_total', 'original_bag', 'stripe_pid',
        'discount', 'discount_amount',
    )

    fields = (
        'order_number', 'user_profile', 'date',
        'full_name', 'email', 'phone_number',
        'discount', 'order_total', 'discount_amount',
        'grand_total', 'original_bag', 'stripe_pid',
        )

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',
                    'grand_total',)

    ordering = ('-date',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Discount model.

    Specifies list display, filters, search fields,
    and marks 'created_on' as read-only.
    """
    list_display = ('code', 'percentage', 'active', 'created_on')
    list_filter = ('active',)
    search_fields = ('code',)
    fields = ('code', 'percentage', 'active', 'created_on')
    readonly_fields = ('created_on',)
