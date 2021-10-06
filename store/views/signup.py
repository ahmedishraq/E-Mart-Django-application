from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


# class for signup
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        # taking the input info from form
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # data validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # creating object of customer class
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = None

        # checking data validation with function
        error_message = self.validateCustomer(customer)

        if (not error_message):
            # Hashing the customer password
            customer.password = make_password(customer.password)

            # appling Customer class register method for register and save
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

        # to get the each input filed data and show in another page
        # return HttpResponse(request.POST.get('email'))

    # Customer data validation
    def validateCustomer(self, customer):
        error_message = None

        if (not customer.first_name):
            error_message = "First Name Required!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 char long or more"
        elif (not customer.last_name):
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 char long or more"
        elif (not customer.phone):
            error_message = "Phone Number required"
        elif len(customer.phone) < 11:
            error_message = "Phone Number must be 11 char long"
        elif len(customer.email) < 5:
            error_message = "Email must be 5 char long"
        elif len(customer.password) < 4:
            error_message = "Password must be 6 char long"
        elif customer.isExists():
            error_message = "Email Address Already Registered..."

        return error_message
