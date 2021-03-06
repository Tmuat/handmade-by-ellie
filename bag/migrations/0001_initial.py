# Generated by Django 3.1.8 on 2021-04-26 10:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeliveryOptions",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("created_by", models.CharField(blank=True, max_length=100)),
                ("updated_by", models.CharField(blank=True, max_length=100)),
                (
                    "sku",
                    models.IntegerField(
                        blank=True, editable=False, unique=True
                    ),
                ),
                ("option", models.CharField(max_length=255)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10
                    ),
                ),
                ("description", models.CharField(max_length=400)),
                (
                    "active",
                    models.BooleanField(
                        choices=[(True, "Active"), (False, "Not Active")],
                        default=False,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Delivery Options",
            },
        ),
    ]
