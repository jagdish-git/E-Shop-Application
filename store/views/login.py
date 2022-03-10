from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import  check_password
from django.views import View

class Login(View):
    return_url= None
    def get(self, request, *args, **kwargs):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                # return redirect('homepage') 
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage') 
            else:
                error_msg = 'Email or Password Invalid !!'
        else:
            error_msg = 'Email or Password Invalid !!'

        return render(request, 'login.html', {'error': error_msg})

def logout(request):
    request.session.clear()
    return redirect('login')