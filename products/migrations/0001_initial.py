# Generated by Django 3.1.8 on 2021-04-19 13:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
    ]