import pytest

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
        image="temp-image.png"
    )
    product.category.add(category)
    return product


@pytest.fixture
def product_stock(product):
    return ProductStock.objects.create(available_stock=100, product=product)
