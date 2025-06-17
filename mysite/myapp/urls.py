from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>', views.detail, name='detail'),
    path('create-checkout-session/<int:id>', views.create_checkout_session, name='api_checkout_session'),
    path('success/', views.payment_success_view, name='success'),
    path('failed/', views.payment_failed_view, name='failed'),
    path('create-product/', views.create_product, name='create_product'),
    path('edit-product/<int:id>', views.product_edit, name='edit_product'),
    path('delete-product/<int:id>', views.product_delete, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
]
