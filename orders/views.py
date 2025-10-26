from django.shortcuts import render
from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=20)

def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # In a real app we'd persist the order; here we mock success
            request.session['cart'] = {}
            return render(request, 'orders/success.html', {'name': form.cleaned_data['full_name']})
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'form': form, 'cart': cart})
