# Generated by Django 3.1.8 on 2021-04-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bag", "0006_auto_20210429_0955"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discountcode",
            name="expiry",
            field=models.DateField(blank=True, null=True),
        ),
    ]
