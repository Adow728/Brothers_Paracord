"""Defines URL patterns for management"""

from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage, name="dashboard"),
    path('manage/products', views.products, name="products"),
    path('manage/products/<id>', views.product, name="view_product"),
    path('manage/order/<id>', views.order, name="view_order"),
    path('manage/employee/<id>', views.employee, name="view_employee"),
    path('manage/sales', views.sales, name="sales"),
]