# Generated by Django 3.1.8 on 2021-04-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="friendly_name",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=254),
            preserve_default=False,
        ),
    ]
