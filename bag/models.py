import uuid

from django.db import models

from common.models import UpdatedAndCreated
from common.utils import unique_sku_generator


class DeliveryOptions(UpdatedAndCreated):
    ACTIVE = (
        (True, "Active"),
        (False, "Not Active"),
    )
    sku = models.IntegerField(
        null=False, blank=True, unique=True, editable=False
    )
    option = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    description = models.CharField(max_length=400, null=False, blank=False)
    active = models.BooleanField(default=False, choices=ACTIVE)

    class Meta:
        verbose_name_plural = "Delivery Options"

    def save(self, *args, **kwargs):
        """
        Override the original save method to set a unique sku
        for the delivery option.
        """
        if not self.sku:
            self.sku = unique_sku_generator(self, 6)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.option


class DiscountCode(models.Model):
    ACTIVE = (
        (True, "Active"),
        (False, "Not Active"),
    )
    TRUE_FALSE = (
        (True, "True"),
        (False, "False"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.IntegerField(
        null=False, blank=True, unique=True, editable=False
    )
    code = models.CharField(max_length=50, blank=False, unique=True)
    discount = models.IntegerField(blank=False, null=False)
    active = models.BooleanField(default=False, choices=ACTIVE)
    set_expiry = models.BooleanField(default=False, choices=TRUE_FALSE)
    set_quantity = models.BooleanField(default=False, choices=TRUE_FALSE)
    expiry = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set a unique sku
        for the discount code.
        """
        if not self.sku:
            self.sku = unique_sku_generator(self, 6)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code
