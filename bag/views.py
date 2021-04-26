from django.utils import timezone

from django.shortcuts import (
    render,
    reverse,
    redirect,
    get_object_or_404,
    HttpResponse,
)

from django.contrib import messages

from bag.models import DeliveryOptions, DiscountCode
from products.models import Product


def view_bag(request):
    """A view to return the bag page"""

    delivery = DeliveryOptions.objects.filter(active=True)

    context = {
        "delivery": delivery,
    }

    return render(request, "bag/bag.html", context)


def add_to_bag(request, product_id):
    """
    Add a quantity of specified product to the shopping bag.
    """
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity"))

    redirect_url = request.POST.get("redirect_url")

    if quantity > product.product_stock.available_stock:
        messages.error(
            request, "There isn't enough stock of the selected product."
        )
        return redirect(redirect_url)

    bag = request.session.get("bag", {})

    if str(product.sku) in list(bag.keys()):
        if bag[str(product.sku)] >= product.product_stock.available_stock:
            messages.error(
                request,
                "There isn't enough stock of the selected product. You may already have some in your bag.",
            )
            return redirect(redirect_url)
        bag[str(product.sku)] += quantity
        messages.success(
            request,
            (
                f"Updated {product.name} "
                f"quantity to {bag[str(product.sku)]}"
            ),
        )
    else:
        bag[product.sku] = quantity
        messages.success(request, f"Added {product.name} to your bag")
    request.session["bag"] = bag

    return redirect(redirect_url)


def adjust_bag(request, product_id):
    """
    Adjust the quantity of specified product to the shopping bag.
    """
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity"))

    if quantity > product.product_stock.available_stock:
        messages.error(
            request, "There isn't enough stock" " of the selected product"
        )
        return redirect("view_bag")

    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[str(product.sku)] = quantity
        messages.success(
            request,
            (
                f"Updated {product.name} "
                f"quantity to {bag[str(product.sku)]}"
            ),
        )
        print("Should have updated", bag)
    else:
        bag.pop(str(product.sku))
        messages.success(
            request, (f"Removed {product.name} " f"from your bag")
        )

    request.session["bag"] = bag

    return redirect(reverse("view_bag"))


def remove_from_bag(request, product_id):
    """
    Remove the item from the shopping bag.
    """

    try:
        product = get_object_or_404(Product, id=product_id)

        bag = request.session.get("bag", {})

        bag.pop(str(product.sku))

        messages.success(request, f"Removed {product.name} from your bag")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)


def add_delivery(request):
    """
    Add the specified delivery option.
    """
    if request.method == "POST":
        selected = request.POST.get("id-selected")

        delivery = get_object_or_404(DeliveryOptions, id=selected)

        delivery_option = request.session.get("delivery", {})

        delivery_option.clear()

        delivery_option["option"] = delivery.sku

        messages.success(
            request, f"{delivery.option} - £{delivery.price} " f"selected."
        )

        print(delivery_option)

        request.session["delivery"] = delivery_option

    return redirect(reverse("view_bag"))


def add_discount(request):
    """
    Check and if valid add the discount code
    """
    if request.method == "POST":
        code = request.POST.get("discount-code")
        discount = request.session.get("discount", {})

        try:
            database_code = DiscountCode.objects.get(code=code)
        except DiscountCode.DoesNotExist:
            messages.error(request, f"'{code}' is not a valid discount code.")
            return redirect(reverse("view_bag"))

        if database_code.active:
            if database_code.set_expiry:
                if timezone.now() < database_code.expiry:
                    if database_code.set_quantity:
                        if database_code.quantity > 0:
                            discount.clear()
                            discount["discount"] = database_code.sku
                            messages.success(
                                request, f"{code} has been applied."
                            )
                            request.session["discount"] = discount
                        else:
                            messages.error(
                                request, f"'{code}' has no valid uses left."
                            )
                            return redirect(reverse("view_bag"))
                    else:
                        discount.clear()
                        discount["discount"] = database_code.sku
                        messages.success(request, f"{code} has been applied.")
                        request.session["discount"] = discount
                else:
                    messages.error(request, f"'{code}' has expired.")
                    return redirect(reverse("view_bag"))
            elif database_code.set_quantity:
                if database_code.quantity > 0:
                    discount.clear()
                    discount["discount"] = database_code.sku
                    messages.success(request, f"{code} has been applied.")
                    request.session["discount"] = discount
                else:
                    messages.error(
                        request, f"'{code}' has no valid uses left."
                    )
                    return redirect(reverse("view_bag"))
            else:
                discount.clear()
                discount["discount"] = database_code.sku
                messages.success(request, f"{code} has been applied.")
                request.session["discount"] = discount
        else:
            messages.error(
                request, f"'{code}' is not an active discount code."
            )
            return redirect(reverse("view_bag"))

    return redirect(reverse("view_bag"))
