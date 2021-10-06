from django.shortcuts import render, redirect
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

        #data validation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }

        # creating object of customer class
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)


        error_message = None

        if(not first_name):
            error_message = "First Name Required!"
        elif len(first_name) < 4:
            error_message = "First name must be 4 char long or more"
        elif (not last_name):
            error_message = "Last Name Required"
        elif len(last_name) < 4:
            error_message = "Last Name must be 4 char long or more"
        elif (not phone):
            error_message = "Phone Number required"
        elif len(phone) < 11:
            error_message = "Phone Number must be 11 char long"
        elif len(email) < 5:
            error_message = "Email must be 5 char long"
        elif len(password) < 4:
            error_message = "Password must be 6 char long"
        elif customer.isExists():
            error_message = "Email Address Already Registered..."



        if (not error_message):
            # appling Customer class register method for register and save
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'signup.html', data)

        # to get the each input filed data and show in another page
        #return HttpResponse(request.POST.get('email'))