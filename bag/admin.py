from django.contrib import admin


from bag.models import DeliveryOptions


class CustomDeliveryOptionsAdmin(admin.ModelAdmin):
    list_display = ('option',
                    'sku',
                    'price',
                    'description',
                    'active',
                    )
    list_filter = ('option', 'price', 'description', 'active',)
    search_fields = ('option',)
    exclude = [
        "updated_by",
        "updated",
        "created_by",
        "created",
    ]


admin.site.register(DeliveryOptions, CustomDeliveryOptionsAdmin)
