import pytest

from products.models import Category


@pytest.fixture
def category() -> Category:
    return Category.objects.create(
        name="test_category", friendly_name="Test Category"
    )
