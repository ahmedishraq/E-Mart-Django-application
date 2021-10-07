from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.


class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        return redirect('homepage')


    def get(self, request):
        products = None
        categories = Category.get_all_categories()

        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories

        # printing in terminal to check the session of the customer's email address
        print("you are: ", request.session.get('customer_email'))

        # return render (request, 'orders/order.html')
        return render(request, 'index.html', data)
