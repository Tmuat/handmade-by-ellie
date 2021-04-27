import pytest

pytestmark = pytest.mark.django_db

# Model testing


def test_order_model(order, delivery):
    """
    A test to check an order method can be created and is created correctly.
    """
    assert order.full_name == "Order Name"
    assert order.email == "Order Email"
    assert order.phone_number == "00000 000 000"
    assert order.country == "GB"
    assert order.postcode == "AA1 1AA"
    assert order.town_or_city == "Town"
    assert order.street_address1 == "2 Order Road"
    assert order.delivery_method == delivery
    assert order.delivery_cost == delivery.price
    assert order.order_total == 10
    assert order.grand_total == 20
    assert order.original_bag == "{}"
    assert order.stripe_pid == "stripe"
    assert order.status == "processing"
    assert str(order) == order.number
