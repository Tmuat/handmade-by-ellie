from django.contrib import admin

from products.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
        "created",
        "created_by",
        "updated",
        "updated_by",
    )
    list_filter = ("created_by",)
    search_fields = (
        "name",
        "created_by",
    )
    exclude = [
        "updated_by",
        "updated",
        "created_by",
        "created",
    ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.email
        obj.updated_by = request.user.email
        obj.save()


admin.site.register(Category, CategoryAdmin)
