from django.contrib import admin


from bag.models import DeliveryOptions, DiscountCode


class CustomDeliveryOptionsAdmin(admin.ModelAdmin):
    list_display = (
        "option",
        "sku",
        "price",
        "description",
        "active",
        "created",
        "created_by",
        "updated",
        "updated_by",
    )
    list_filter = (
        "option",
        "price",
        "description",
        "active",
    )
    search_fields = ("option",)
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


admin.site.register(DeliveryOptions, CustomDeliveryOptionsAdmin)


class CustomDiscountCodeAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "sku",
        "discount",
        "active",
        "quantity",
        "expiry",
        "created",
        "created_by",
    )
    list_filter = (
        "code",
        "active",
    )
    search_fields = ("code",)
    exclude = [
        "created_by",
        "created",
    ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user.email
        obj.updated_by = request.user.email
        obj.save()


admin.site.register(DiscountCode, CustomDiscountCodeAdmin)
