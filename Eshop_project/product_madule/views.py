from django.shortcuts import render, get_object_or_404
from .models import product
from django.http import Http404

def product_list(request):
    products = product.objects.all()
    return render(request, 'product_madule/product_list.html', {
        'products': products
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
