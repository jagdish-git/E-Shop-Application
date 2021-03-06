from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # print(request.session.get('cart'))
        # print(request.session.get('email'))
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})