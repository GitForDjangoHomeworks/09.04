from django.urls import path
from .views import OrderPayment, order_create, OrderDetailView
app_name = 'orders'
urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('<int:pk>/qr/', OrderPayment.as_view(), name='order_qr'),
    path('<int:pk>/detail/', OrderDetailView.as_view(), name='order_detail'),
]