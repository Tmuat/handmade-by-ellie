from django.db import models

from common.models import UpdatedAndCreated


class Category(UpdatedAndCreated):

    class Meta:
        verbose_name_plural = 'Categories'

