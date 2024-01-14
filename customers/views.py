from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # create a user account
            user = User.objects.create(
                username=username,
                password=password,
                email=email
            )
            # create a customer account
            customer = Customer.objects.create(
                user=user,
                address=address,
                phone=phone
            )
            return redirect('home')
        except Exception as e:
            error_message = "Duplicate Username or Invalid Credentials"
            messages.error(request, error_message)
    return render(request, 'account.html')

