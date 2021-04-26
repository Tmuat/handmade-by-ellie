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


# View testing


def test_bag_view_uses_correct_template(client):
    response = client.get("/bag/")
    assertTemplateUsed(response, "bag/bag.html")
