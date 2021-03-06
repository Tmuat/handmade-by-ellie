from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.admin_home, name="admin_home"),
    path("orders/", views.all_orders, name="admin_orders"),
    path("order/<order_number>/", views.order_detail, name="order_detail"),
    path("dispatch/", views.dispatch_orders, name="dispatch_orders"),
    path("complete/", views.complete_orders, name="complete_orders"),
    path("products/", views.all_products, name="admin_products"),
    path("add-product/", views.admin_add_product, name="admin_add_product"),
    path(
        "edit/<product_slug>/",
        views.admin_edit_product,
        name="admin_edit_product",
    ),
    path("delete/<product_id>/", views.delete_product, name="delete_product"),
    path(
        "edit-delivery/", views.admin_edit_delivery, name="admin_edit_delivery"
    ),
    path(
        "edit-discount/", views.admin_edit_discount, name="admin_edit_discount"
    ),
]
