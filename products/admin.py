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

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.username
        obj.updated_by = request.user.username
        obj.save()


admin.site.register(Category, CategoryAdmin)
