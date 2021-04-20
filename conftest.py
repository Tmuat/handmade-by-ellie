import pytest

from products.models import Category, Product


@pytest.fixture
def category() -> Category:
    return Category.objects.create(
        name="test_category", friendly_name="Test Category"
    )


@pytest.fixture
def product(category) -> Product:
    return Product.objects.create(
        sku=25545, name="Test Product", category=category,
        description="Test description", price=10, slug="test-product"
    )
