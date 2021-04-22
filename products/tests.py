import pytest

from pytest_django.asserts import assertTemplateUsed

from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from products.admin import CategoryAdmin, ProductAdmin
from products.models import Category, Product

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


class MockRequest(object):
    """
    Used to create a mock request for the override of admin save.
    """

    def __init__(self, user=None):
        self.user = user


def test_category_admin_save(client):
    """
    Used to test that the save_model override sets the user email on
    admin save. It tests the created_by field is set.
    """
    User = get_user_model()
    admin_user = User.objects.create_superuser("super@user.com", "foo")

    category_model_admin = CategoryAdmin(
        model=Category, admin_site=AdminSite()
    )
    category_model_admin.save_model(
        obj=Category(name="test_category"),
        request=MockRequest(user=admin_user),
        form=None,
        change=None,
    )

    category = get_object_or_404(Category, name="test_category")

    assert category.created_by == "super@user.com"


def test_category_admin_save_updated_by(client, category):
    """
    Used to test that the save_model override sets the user email on
    admin save. It checks the updated_by field is set correctly
    """
    User = get_user_model()
    second_admin_user = User.objects.create_superuser(
        "second_super@user.com", "foo"
    )

    category.created_by = "super@user.com"
    category.save()

    category_model_admin = CategoryAdmin(
        model=Category, admin_site=AdminSite()
    )
    category_model_admin.save_model(
        obj=category,
        request=MockRequest(user=second_admin_user),
        form=None,
        change=None,
    )

    assert category.created_by == "super@user.com"
    assert category.updated_by == "second_super@user.com"


def test_product_model(product, category):
    """
    Tests the creation of instances in the product model.
    """
    assert product.sku == 25545
    assert product.name == "Test Product"
    assert product.category.first() == category
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


def test_product_admin_save(client, category):
    """
    Used to test that the save_model override sets the user email on
    admin save. It checks the created_by field is set.
    """
    User = get_user_model()
    admin_user = User.objects.create_superuser("super@user.com", "foo")

    product_model_admin = ProductAdmin(model=Product, admin_site=AdminSite())
    product_model_admin.save_model(
        obj=Product(
            sku=25545,
            name="Test Product",
            description="Test description",
            price=10,
            slug="test-product",
        ),
        request=MockRequest(user=admin_user),
        form=None,
        change=None,
    )

    product = get_object_or_404(Product, name="Test Product")

    assert product.created_by == "super@user.com"


def test_product_admin_save_updated_by(client, product):
    """
    Used to test that the save_model override sets the user email on
    admin save. It checks the updated_by field is set correctly
    """
    User = get_user_model()
    second_admin_user = User.objects.create_superuser(
        "second_super@user.com", "foo"
    )

    product.created_by = "super@user.com"
    product.save()

    product_model_admin = ProductAdmin(model=Product, admin_site=AdminSite())
    product_model_admin.save_model(
        obj=product,
        request=MockRequest(user=second_admin_user),
        form=None,
        change=None,
    )

    assert product.created_by == "super@user.com"
    assert product.updated_by == "second_super@user.com"


# View testing


def test_all_products_view_uses_correct_template(client):
    response = client.get("/products/")
    assertTemplateUsed(response, "products/products.html")


def test_all_products_context_data(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert "products" in response.context
    assert "search_term" in response.context
    assert "current_categories" in response.context
    assert "current_sorting" in response.context


def test_product_detail_view_uses_correct_template(client, product):
    detail_url = f"/products/item/{product.slug}/"
    print(detail_url)
    response = client.get(detail_url)
    assertTemplateUsed(response, "products/product_detail.html")


def test_product_detail_context_data(client, product):
    detail_url = f"/products/item/{product.slug}/"
    response = client.get(detail_url)
    assert response.status_code == 200
    assert "product" in response.context


def test_product_detail_no_product(client, product):
    response = client.get("/products/item/a-product/")
    assert response.status_code == 404
