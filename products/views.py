from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
