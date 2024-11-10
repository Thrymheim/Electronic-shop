from . import views
from django.urls import path

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('<slug:slug>', views.product_detail, name='product-detail'),
]
