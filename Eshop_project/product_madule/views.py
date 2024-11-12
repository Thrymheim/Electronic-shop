from django.shortcuts import render, get_object_or_404
from .models import product
from django.http import Http404
from django.db.models import Avg
def product_list(request):
    products = product.objects.all().order_by('title') #put - before it and it becomes reverse
    totall_number_of_products = products.count()
    average_rating = products.aggregate(Avg('rating')) #we named it rating at models
    return render(request, 'product_madule/product_list.html', {
        'products': products,
        'totall_number_of_products': totall_number_of_products,
        'average_rating': average_rating

    })
def product_detail(request,slug):
    # try:
    #     detail_product = product.objects.get(id=product_id)
    # except:
    #     raise Http404("Product does not exist")
    detail_product=get_object_or_404(product,slug=slug) #pk = primary key = id
    return render(request, 'product_madule/product_detail.html', {
        'detail_product': detail_product
    })
