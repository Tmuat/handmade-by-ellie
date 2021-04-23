from django.shortcuts import get_object_or_404

from products.models import Product


def bag_contents(request):

    bag_items = []

    total = 0
    delivery_cost = 0
    grand_total = 0
    product_count = 0

    bag = request.session.get('bag', {})

    for product_sku, quantity in bag.items():
        product = get_object_or_404(Product, sku=product_sku)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_sku': product_sku,
            'quantity': quantity,
            'product': product
            })

    grand_total = total + delivery_cost

    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'grand_total': grand_total
    }

    return context
