from django.contrib import admin
from .models import Order, OrderLineItem, Discount


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',
                       'original_bag', 'stripe_pid',
                       'discount', 'discount_amount',)

    fields = ('order_number', 'user_profile', 'date',
              'full_name', 'email', 'phone_number',
              'discount', 'order_total', 'discount_amount',
              'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',
                    'grand_total',)

    ordering = ('-date',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'percentage', 'active', 'created_on')
    list_filter = ('active',)
    search_fields = ('code',)
    fields = ('code', 'percentage', 'active', 'created_on')
    readonly_fields = ('created_on',)
