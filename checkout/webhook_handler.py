import json
import time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from bag.models import DeliveryOptions, DiscountCode
from checkout.models import Order, OrderLineItem
from products.models import Product, ProductStock


class StripeWH_Handler:
    """ Handles webhooks from stripe"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic or unknown webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        delivery_option = intent.metadata.delivery
        discount_code = intent.metadata.discount

        delivery_json = json.loads(delivery_option)
        delivery_sku = delivery_json.get("option")
        delivery = get_object_or_404(DeliveryOptions, sku=delivery_sku)

        discount_json = json.loads(discount_code)
        discount_used = False
        if discount_json != {}:
            discount_sku = discount_json.get("discount")
            discount = get_object_or_404(DiscountCode, sku=discount_sku)
            discount_used = True

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | SUCCESS: '
                    "Verified order already in database"
                ),
                status=200,
            )
        else:
            print("Cant find the order")
            order = None
            try:
                if discount_used:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        delivery_method=delivery,
                        delivery_cost=delivery.price,
                        discount=discount,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    if discount.set_quantity:
                        discount.quantity = discount.quantity - 1
                        discount.save()
                else:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        delivery_method=delivery,
                        delivery_cost=delivery.price,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                for product_sku, quantity in json.loads(bag).items():
                    product = Product.objects.get(sku=product_sku)
                    product_stock = ProductStock.objects.get(product=product)
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | SUCCESS: '
                "Created order in webhook"
            ),
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle if a payment failed comes from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )
