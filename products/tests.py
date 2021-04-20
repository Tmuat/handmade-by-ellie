import pytest

from pytest_django.asserts import assertTemplateUsed

from products.models import Category

pytestmark = pytest.mark.django_db


# Model testing

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
    """
    Tests the creation of instances in the product model.
    """
    assert product.sku == 25545
    assert product.name == "Test Product"
    assert product.category == category
    assert product.description == "Test description"
    assert product.price == 10
    assert product.slug == "test-product"


def test_product_model_str(product):
    """
    Tests the product models str method works.
    """
    assert str(product) == "Test Product"


def test_product_stock_model(product_stock, product):
    """
    Tests the product stock model instance creation.
    """
    assert product_stock.available_stock == 100
    assert product_stock.product == product


# View testing

def test_all_products_view_uses_correct_template(client):
    response = client.get('/products/')
    assertTemplateUsed(response, 'products/products.html')


def test_all_products_context_data(client):
    response = client.get('/products/')
    assert response.status_code == 200
    assert 'products' in response.context
