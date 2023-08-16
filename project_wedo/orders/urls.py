from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('approve/<int:order_id>/', views.approve_order, name='approve_order'),
    path('order/<int:order_id>/', views.create_transaction, name='create_transaction'),
]
