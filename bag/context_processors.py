from decimal import Decimal

from django.shortcuts import get_object_or_404

from bag.models import DeliveryOptions, DiscountCode
from products.models import Product


def bag_contents(request):

    bag_items = []
    delivery_option = None
    discount_code = None

    total = 0
    delivery_cost = 0
    grand_total = 0
    product_count = 0

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
        discount_amount = 1 - Decimal(float(discount.discount)) / 100
        total = total * discount_amount
        discount_code = discount
        discount_set = True

    else:
        discount_set = False

    grand_total = total + delivery_cost

    context = {
        "bag_items": bag_items,
        "product_count": product_count,
        "total": total,
        "grand_total": grand_total,
        "delivery_option": delivery_option,
        "delivery_set": delivery_set,
        "discount_set": discount_set,
        "discount_code": discount_code,
    }

    return context
