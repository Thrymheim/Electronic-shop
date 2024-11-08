from django.shortcuts import render
from .models import product


def product_list(request):
    products = product.objects.all()
    return render(request, 'product_madule/product_list.html', {
        'products': products
    })