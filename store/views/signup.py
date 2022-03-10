from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        
        values = {'first_name':first_name, 'last_name':last_name,
                'phone':phone, 'email':email}

        error_msg = None
        customer = Customer(first_name=first_name, last_name=last_name, 
                            phone=phone, email=email,password=password)
        
        error_msg = self.validate_customer(customer)
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {'error': error_msg, 'values' : values}
            return render(request, 'signup.html', data)

    def validate_customer(self, customer):
        error_msg = None
        if not customer.first_name:
            error_msg = 'First Name Required !!!'
        elif len(customer.first_name) < 4:
            error_msg = 'First Name must be 4 character or more'    
        elif not customer.last_name:
            error_msg = 'Last Name Required !!!'
        elif len(customer.last_name) < 2:
            error_msg = 'Last Name must be two character long'   
        elif not customer.phone:
            error_msg = 'Phone Number Required !!!'
        elif len(customer.phone) < 10 :
            error_msg = 'Phone must have 10 numbers.'
        elif not customer.email:
            error_msg = '@Email is Required !'
        elif not customer.password:
            error_msg = 'Password must required..'
        elif len(customer.password) < 6:
            error_msg = 'Password must be 6 character long..'
        if customer.isExists():
            error_msg = "This Email Already Registered."
        return error_msg
