from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.

# def for product
def index(request):

    products = None
    categories = Category.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products();

    data={}
    data['products'] = products
    data['categories'] = categories

    #return render (request, 'orders/order.html')
    return render (request, 'index.html', data)

# def for signup page
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        # taking the input info from form
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # creating object of customer class
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            phone = phone,
                            email = email,
                            password = password)

        # appling Customer class register method for register and save
        customer.register()

        return HttpResponse("Signup Successfully!")

        # to get the each input filed data and show in another page
        #return HttpResponse(request.POST.get('email'))