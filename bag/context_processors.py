from decimal import Decimal

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils import timezone

from bag.models import DeliveryOptions, DiscountCode
from products.models import Product, ProductStock


def bag_contents(request):

    bag_items = []
    delivery_option = None
    discount_code = None

    total = 0
    delivery_cost = 0
    grand_total = 0
    product_count = 0
    products_in_stock = True
    discount_valid = False
    discount_set = False

    bag = request.session.get("bag", {})
    delivery_array = request.session.get("delivery", {})
    discount = request.session.get("discount", {})

    for product_sku, quantity in bag.items():
        product = get_object_or_404(Product, sku=product_sku)
        total += quantity * product.price
        product_count += quantity
        bag_items.append(
            {
                "product_sku": product_sku,
                "quantity": quantity,
                "product": product,
            }
        )
        product_stock = ProductStock.objects.get(product=product)
        if quantity > product_stock.available_stock:
            products_in_stock = False

    delivery_sku = delivery_array.get("option")
    if delivery_sku is not None:
        delivery = get_object_or_404(DeliveryOptions, sku=delivery_sku)
        delivery_cost = delivery.price
        delivery_option = delivery
        delivery_set = True
    else:
        delivery_set = False

    discount_code = discount.get("discount")
    if discount_code is not None:
        discount = get_object_or_404(DiscountCode, sku=discount_code)
        if discount.active:
            if discount.set_expiry:
                if timezone.now() < discount.expiry:
                    if discount.set_quantity:
                        if discount.quantity > 0:
                            discount_amount = (
                                1 - Decimal(float(discount.discount)) / 100
                            )
                            total = total * discount_amount
                            discount_code = discount
                            discount_valid = True
                            discount_set = True
                        else:
                            messages.error(
                                request,
                                f"'{discount.code}' has no valid uses left."
                                " It has been removed.",
                            )
                            del request.session["discount"]
                    else:
                        discount_amount = (
                            1 - Decimal(float(discount.discount)) / 100
                        )
                        total = total * discount_amount
                        discount_code = discount
                        discount_valid = True
                        discount_set = True
                else:
                    messages.error(
                        request,
                        f"'{discount.code}' has expired."
                        "  It has been removed.",
                    )
                    del request.session["discount"]
            elif discount.set_quantity:
                if discount.quantity > 0:
                    discount_amount = (
                        1 - Decimal(float(discount.discount)) / 100
                    )
                    total = total * discount_amount
                    discount_code = discount
                    discount_valid = True
                    discount_set = True
                else:
                    messages.error(
                        request,
                        f"'{discount.code}' has no valid uses left."
                        "  It has been removed.",
                    )
                    del request.session["discount"]
            else:
                discount_amount = 1 - Decimal(float(discount.discount)) / 100
                total = total * discount_amount
                discount_code = discount
                discount_valid = True
                discount_set = True
        else:
            messages.error(
                request,
                f"'{discount.code}' is not an active discount code."
                "  It has been removed.",
            )
            del request.session["discount"]

    grand_total = total + delivery_cost

    context = {
        "bag_items": bag_items,
        "product_count": product_count,
        "product_stock": products_in_stock,
        "total": total,
        "grand_total": grand_total,
        "delivery_option": delivery_option,
        "delivery_set": delivery_set,
        "discount_set": discount_set,
        "discount_code": discount_code,
        "discount_valid": discount_valid,
    }

    return context
