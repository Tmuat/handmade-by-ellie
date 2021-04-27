from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from checkout.forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    delivery_option = request.session.get('delivery', {})
    discount = request.session.get("discount", {})

    if not bag:
        messages.error(request,
                       "There is nothing in your bag at the moment")
        return redirect(reverse('bag'))

    if not delivery_option:
        messages.error(request,
                       "There is no delivery option selected")
        return redirect(reverse('bag'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
