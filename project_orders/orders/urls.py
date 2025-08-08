from django.urls import path
from .views import list_orders, get_order, order_status

urlpatterns = [
    path('orders/', list_orders),
    path('orders/<int:order_id>/', get_order),
    path('orders/status/', order_status),
]