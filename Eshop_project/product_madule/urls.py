from . import views
from django.urls import path

urlpatterns = [
    path('', views.product_list, name='list'),
]
