from django.db import models

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

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.IntegerField(null=True,
                              blank=True,
                              unique=True,
                              editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(null=False,
                            unique=True)
    image = models.ImageField(blank=True)
