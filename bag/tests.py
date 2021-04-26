import pytest

from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db

# Model testing


def test_delivery_model(delivery):
    """
    A test to check a delivery method can be created and is created correctly.
    """
    assert delivery.option == "Delivery Option"
    assert delivery.price == 10
    assert delivery.description == "Delivery Desc"
    assert delivery.active is True
    assert str(delivery) == "Delivery Option"


def test_discount_code_model(code):
    """
    A test to check a discount code can be created and is created correctly.
    """
    assert code.code == "TESTCODE"
    assert code.discount == 5
    assert code.active is True
    assert code.set_expiry is False
    assert code.set_quantity is False
    assert str(code) == "TESTCODE"


# View testing


def test_bag_view_uses_correct_template(client):
    response = client.get("/bag/")
    assertTemplateUsed(response, "bag/bag.html")


def test_bag_context_data(client):
    response = client.get("/bag/")
    assert response.status_code == 200
    assert "delivery" in response.context
