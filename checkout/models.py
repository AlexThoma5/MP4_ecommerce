import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum

from services.models import Service
from profiles.models import UserProfile


class Discount(models.Model):
    code = models.CharField(max_length=16, unique=True, null=False,
                            blank=False)
    percentage = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to strip and convert the
        discount code to uppercase.
        """
        self.code = self.code.strip().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.code} - %{self.percentage}'


class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="orders"
    )
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')
    discount = models.ForeignKey(
        Discount, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='orders'
    )
    discount_amount = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for discounts.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.discount and self.discount.active:
            self.discount_amount = round(
                self.order_total * Decimal(self.discount.percentage / 100), 2)
        else:
            self.discount_amount = 0

        self.grand_total = self.order_total - self.discount_amount
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.service.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.service.name} on order {self.order.order_number}'
