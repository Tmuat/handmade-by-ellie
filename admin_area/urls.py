from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.admin_home, name="admin_home"),
    path("orders/", views.all_orders, name="admin_orders"),
    path("order/<order_number>/", views.order_detail, name="order_detail"),
    path("dispatch/", views.dispatch_orders, name="dispatch_orders"),
]
