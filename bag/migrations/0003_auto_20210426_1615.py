# Generated by Django 3.1.8 on 2021-04-26 15:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bag", "0002_discountcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discountcode",
            name="quantity",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
