from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages

from products.models import Product


def view_bag(request):
    """A view to return the bag page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, product_id):
    """
    Add a quantity of specified product to the shopping bag.
    """
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')

    if quantity > product.product_stock.available_stock:
        messages.error(request, "There isn't enough stock"
                                " of the selected product")
        return redirect(redirect_url)

    bag = request.session.get('bag', {})

    if product.sku in list(bag.keys()):
        bag[product.sku] += quantity
        messages.success(request,
                         (f'Updated {product.name} '
                          f'quantity to {bag[product.sku]}'))
    else:
        bag[product.sku] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)
