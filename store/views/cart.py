from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product


# class for login (wiil handle GET and POST method)
class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products' : products})