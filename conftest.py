import pytest

from products.models import Category, Product, ProductStock


@pytest.fixture
def category() -> Category:
    return Category.objects.create(
        name="test_category", friendly_name="Test Category"
    )


@pytest.fixture
def product(category) -> Product:
    return Product.objects.create(
        sku=25545, name="Test Product", category=category,
        description="Test description", price=10, slug="test-product",
    )


@pytest.fixture
def product_stock(product):
    product_stock = ProductStock.objects.get(product=product)
    product_stock.available_stock = 100
    product_stock.save()
    return product_stock
