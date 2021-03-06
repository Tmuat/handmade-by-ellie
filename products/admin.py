from django.contrib import admin

from products.models import Category, Product, ProductStock


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


class ProductStockAdminInline(admin.TabularInline):
    model = ProductStock


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductStockAdminInline,)
    list_display = (
        "sku",
        "name",
        "price",
        "image",
        "product_stock",
        "created",
        "created_by",
        "updated",
        "updated_by",
    )

    ordering = ("sku",)

    list_filter = ("category",)

    prepopulated_fields = {"slug": ("name",)}

    search_fields = (
        "name",
        "category",
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


admin.site.register(Product, ProductAdmin)
