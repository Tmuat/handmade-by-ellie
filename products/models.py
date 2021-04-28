import uuid

from django.db import models

from common.models import UpdatedAndCreated
from common.utils import unique_sku_generator


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
    ACTIVE = (
        (True, "Active"),
        (False, "Not Active"),
    )

    class Meta:
        verbose_name_plural = "Products"

    category = models.ManyToManyField(Category)
    sku = models.IntegerField(
        null=False, blank=True, unique=True, editable=False
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(null=False, blank=False)
    active = models.BooleanField(default=True, choices=ACTIVE)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set a unique sku for the product.
        """
        if not self.sku:
            self.sku = unique_sku_generator(self, 5)
        super().save(*args, **kwargs)

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
