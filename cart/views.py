from django.shortcuts import render, redirect
from products.models import Product
from decimal import Decimal

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = Decimal('0.00')
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=pid)
            line_total = product.price * qty
            items.append({'product': product, 'qty': qty, 'line_total': line_total})
            total += line_total
        except Product.DoesNotExist:
            continue
    return render(request, 'cart/view_cart.html', {'items': items, 'total': total})

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('view_cart')

def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        if action == 'add':
            cart[pid] += 1
        elif action == 'remove':
            cart[pid] -= 1
            if cart[pid] <= 0:
                del cart[pid]
    request.session['cart'] = cart
    return redirect('view_cart')
