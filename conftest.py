import pytest

from bag.models import DeliveryOptions, DiscountCode
from products.models import Category, Product, ProductStock


@pytest.fixture
def category() -> Category:
    return Category.objects.create(
        name="test_category", friendly_name="Test Category"
    )


@pytest.fixture
def product(category) -> Product:
    product = Product.objects.create(
        sku=25545,
        name="Test Product",
        description="Test description",
        price=10,
        slug="test-product",
        image="temp-image.png",
    )
    product.category.add(category)
    return product


@pytest.fixture
def product_stock(product):
    return ProductStock.objects.create(available_stock=100, product=product)


@pytest.fixture
def delivery():
    return DeliveryOptions.objects.create(
        option="Delivery Option",
        price=10,
        description="Delivery Desc",
        active=True,
    )


def code():
    return DiscountCode.objects.create(
        code="TESTCODE", active=True, set_expiry=False,
        set_quantity=False, discount=5
    )
