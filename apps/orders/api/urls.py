from django.urls import path 
from . import orders as views

urlpatterns = [
    path('', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
]