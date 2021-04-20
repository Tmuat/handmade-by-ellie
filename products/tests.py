import pytest

from products.models import Category, Product

pytestmark = pytest.mark.django_db


def test_category_model(category):
    """
    A test to check a category can be created and is created correctly.
    It then checks the model str and get friendly name work.
    """
    assert category.name == "test_category"
    assert category.friendly_name == "Test Category"
    assert str(category) == "test_category"
    assert category.get_friendly_name() == "Test Category"


def test_category_friendly_name_null():
    """
    Checks that a category can be created with just a name and no
    friendly name.
    """
    category = Category.objects.create(name="test_category")
    assert category.name == "test_category"
    assert category.friendly_name == ""


def test_product_model(product, category):
    assert product.sku == 25545
    assert product.name == "Test Product"
    assert product.category == category
    assert product.description == "Test description"
    assert product.price == 10
    assert product.slug == "test-product"


# def test_product_model_str(category):
