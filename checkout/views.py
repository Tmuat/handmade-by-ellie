import json
import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.views.decorators.http import require_POST
from django.utils import timezone

from bag.context_processors import bag_contents
from bag.models import DeliveryOptions, DiscountCode
from checkout.forms import OrderForm
from checkout.models import OrderLineItem, Order
from products.models import Product, ProductStock
from users.forms import UserProfileForm
from users.models import UserProfile


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})
        delivery_option = request.session.get("delivery", {})
        discount_session = request.session.get("discount", {})

        delivery_sku = delivery_option.get("option")
        delivery = get_object_or_404(DeliveryOptions, sku=delivery_sku)
        delivery_cost = delivery.price

        discount_code = discount_session.get("discount")
        discount_included = False
        if discount_code is not None:
            discount = get_object_or_404(DiscountCode, sku=discount_code)
            discount_included = True

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.delivery_cost = delivery_cost
            order.delivery_method = delivery
            if discount_included:
                order.discount = discount
            order.save()
            for product_sku, quantity in bag.items():
                try:
                    product = Product.objects.get(sku=product_sku)
                    if product.active is False:
                        messages.info(request, 'Sorry, you have a product '
                                      ' that is no longer for sale. Please '
                                      'check back in the future.')
                        return redirect("checkout")
                    product_stock = ProductStock.objects.get(product=product)
                    if quantity > product_stock.available_stock:
                        messages.error(
                            request,
                            "There is a stock error!"
                            " Please contact support",
                        )
                        return redirect("checkout")
                    else:
                        product_stock.available_stock = (
                            product_stock.available_stock - quantity
                        )
                        product_stock.save()

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your bag wasn't "
                            "found in our database. "
                            "Please contact us for help!"
                        ),
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))

            if discount_included:
                if discount.active:
                    if discount.set_expiry:
                        if timezone.now() < discount.expiry:
                            if discount.set_quantity:
                                if discount.quantity > 0:
                                    discount.quantity = discount.quantity - 1
                                    discount.save()
                                else:
                                    messages.error(
                                        request,
                                        f"'{discount.code}' has no "
                                        "valid uses left.",
                                    )
                                    del request.session["discount"]
                                    order.delete()
                                    return redirect(reverse("view_bag"))
                        else:
                            messages.error(
                                request, f"'{discount.code}' has expired."
                            )
                            del request.session["discount"]
                            order.delete()
                            return redirect(reverse("view_bag"))
                    elif discount.set_quantity:
                        if discount.quantity > 0:
                            discount.quantity = discount.quantity - 1
                            discount.save()
                        else:
                            messages.error(
                                request,
                                f"'{discount.code}' has no valid uses left.",
                            )
                            del request.session["discount"]
                            order.delete()
                            return redirect(reverse("view_bag"))
                else:
                    messages.error(
                        request,
                        f"'{discount.code}' is not an active discount code.",
                    )
                    del request.session["discount"]
                    order.delete()
                    return redirect(reverse("view_bag"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                (
                    "There was an error with your form. "
                    "Please double check your information."
                ),
            )
    else:
        bag = request.session.get("bag", {})
        delivery_option = request.session.get("delivery", {})
        discount_session = request.session.get("discount", {})

        if not bag:
            messages.error(
                request, "There is nothing in your bag at the moment"
            )
            return redirect(reverse("view_bag"))

        if not delivery_option:
            messages.error(request, "There is no delivery option selected")
            return redirect(reverse("view_bag"))

        for product_sku, quantity in bag.items():
            product = Product.objects.get(sku=product_sku)
            if product.active is False:
                messages.info(request, 'Sorry, you have a product '
                              ' that is no longer for sale. Please '
                              'check back in the future.')
                return redirect("checkout")
            product_stock = ProductStock.objects.get(product=product)
            if quantity > product_stock.available_stock:
                messages.error(
                    request,
                    "There is a stock error!" " Please contact support",
                )
                return redirect(reverse("view_bag"))

        discount_code = discount_session.get("discount")
        discount_included = False
        if discount_code is not None:
            discount = get_object_or_404(DiscountCode, sku=discount_code)
            discount_included = True

        if discount_included:
            if discount.active:
                if discount.set_expiry:
                    if timezone.now() < discount.expiry:
                        if discount.set_quantity:
                            if discount.quantity > 0:
                                pass
                            else:
                                messages.error(
                                    request,
                                    f"'{discount.code}' has no "
                                    "valid uses left.",
                                )
                                del request.session["discount"]
                                return redirect(reverse("view_bag"))
                    else:
                        messages.error(
                            request, f"'{discount.code}' has expired."
                        )
                        del request.session["discount"]
                        return redirect(reverse("view_bag"))
                elif discount.set_quantity:
                    if discount.quantity > 0:
                        pass
                    else:
                        messages.error(
                            request,
                            f"'{discount.code}' has no valid uses left.",
                        )
                        del request.session["discount"]
                        return redirect(reverse("view_bag"))
                else:
                    pass
            else:
                messages.error(
                    request,
                    f"'{discount.code}' is not an active discount code.",
                )
                del request.session["discount"]
                return redirect(reverse("view_bag"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total, currency=settings.STRIPE_CURRENCY
        )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(
                initial={
                    "full_name": profile.user.get_full_name(),
                    "email": profile.user.email,
                    "phone_number": profile.default_phone_number,
                    "country": profile.default_country,
                    "postcode": profile.default_postcode,
                    "town_or_city": profile.default_town_or_city,
                    "street_address1": profile.default_street_address1,
                    "street_address2": profile.default_street_address2,
                    "county": profile.default_county,
                }
            )
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    template = "checkout/checkout.html"

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts.
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    if "delivery" in request.session:
        del request.session["delivery"]

    if "discount" in request.session:
        del request.session["discount"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "delivery": json.dumps(request.session.get("delivery", {})),
                "discount": json.dumps(request.session.get("discount", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            (
                "Sorry, your payment cannot be "
                "processed at the moment. Please try "
                "again later."
            ),
        )
        return HttpResponse(content=e, status=400)
