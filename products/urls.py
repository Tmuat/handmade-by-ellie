from django.urls import path
from products import views

urlpatterns = [
    path("", views.all_products, name="all_products"),
    path("item/<product_slug>/", views.product_detail, name="product_detail"),
]
