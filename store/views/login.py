from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


# class for login (wiil handle GET and POST method)
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                #Saving a customer for session
                request.session['customer'] = customer.id
                #redirect to next page
                return redirect('homepage')
            else:
                error_message = "Email or Password invalid !!"
                return render(request, 'login.html', {'error': error_message})
        else:
            error_message = "Email or Password invalid !!"
            return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')
