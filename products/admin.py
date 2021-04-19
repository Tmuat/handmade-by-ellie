from django.contrib import admin

from products.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'created',
        'created_by',
        'updated',
        'updated_by'
    )


admin.site.register(Category, CategoryAdmin)
