import uuid

from decimal import Decimal
from django_countries.fields import CountryField

from django.db import models
from django.db.models import Sum

from bag.models import DeliveryOptions, DiscountCode
from common.utils import unique_order_generator
from products.models import Product
from users.models import UserProfile


class Order(models.Model):
    STATUS = (
        ("processing", "Processing"),
        ("dispatched", "Dispatched"),
        ("complete", "Complete"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    order_number = models.IntegerField(
        null=False, blank=True, unique=True, editable=False
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_method = models.ForeignKey(
        DeliveryOptions,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="delivery_option",
    )
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    discount = models.ForeignKey(
        DiscountCode,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="discount_code",
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )
    status = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="processing",
        choices=STATUS,
    )

    def update_total(self):
        """
        Update grand total each time a line item is added,
        adding in delivery costs & any discount the orderer has.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )
        if self.discount:
            discount_amount = 1 - Decimal(float(self.discount.discount)) / 100
            self.order_total = self.order_total * discount_amount
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to create a unique order number.
        """
        if not self.order_number:
            self.order_number = unique_order_generator(self, 8)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order_number)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to set the lineitem total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.product.sku} on order {self.order.order_number}"
