import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from common.models import UpdatedAndCreated


class Category(UpdatedAndCreated):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(UpdatedAndCreated):
    class Meta:
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.IntegerField(
        null=True, blank=True, unique=True, editable=False
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class ProductStock(models.Model):
    class Meta:
        verbose_name = "Product Stock"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available_stock = models.IntegerField(null=False, blank=False, default=0)
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="product_stock",
    )

    def __str__(self):
        return str(self.available_stock)
