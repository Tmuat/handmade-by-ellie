# Generated by Django 3.1.8 on 2021-04-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210422_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.IntegerField(blank=True, editable=False, unique=True),
        ),
    ]