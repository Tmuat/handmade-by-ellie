# Generated by Django 3.1.8 on 2021-04-20 14:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210420_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Product Stock',
            },
        ),
    ]