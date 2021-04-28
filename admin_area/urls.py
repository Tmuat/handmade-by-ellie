from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.admin_home, name='admin_home'),
    path('orders/',
         views.all_orders,
         name='admin_orders'),
]
