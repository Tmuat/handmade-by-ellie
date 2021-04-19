import pytest

from products.models import Category

pytestmark = pytest.mark.django_db


def test_category_model():
    category = Category.objects.create(
        name="test_category",
        friendly_name="Test Category"
    )
    assert category.name == "test_category"
    assert category.friendly_name == "Test Category"
