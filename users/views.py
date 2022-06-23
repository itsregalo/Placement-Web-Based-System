from datetime import datetime
from distutils.ccompiler import gen_lib_options
from django.shortcuts import redirect, render
from psutil import users
from pytz import utc
from applications.models import Application
from attachments.models import Attachment
from config.sms import send_otp_to_validate_phone

from users.models import Account

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.hashers import make_password

def index(request):
    username = password = ''

    if request.method == "POST":
        password = request.POST['password']
        email = request.POST['email']
        print(email)
        print(password)



        if password == "1234" and email == "1234@gmail.com":
            return redirect('users:org_home')
            print("Fuck")
        
        if password == "12345" and email=="12345@gmail.com":
            return redirect('users:customer_home')
            print("Fuck2")
            

        # # password = make_password('password')
        # # print(password)

        # user = authenticate(username=email, password=password)
        # # if user is not None:
        # login(request,user)
        # print("Authenticated")
        # acc = Account.objects.all()

        # if request.user.is_organization == True:
        #     redirect('users:org_home')

        # if request.user.is_student == True:
        #     redirect('users:customer_home')

        # if user.is_authenticated:
        #     return redirect('users:customer_home')


    return render(request, 'index.html')

def customer_home(request):
    attacments = Attachment.objects.all().order_by('-id')
    applications = Application.objects.all()

    
    data = {
        'users': None,
        'attacments': attacments,
    }
    return render(request, 'attachments.html',data)

def chat(request):
    return render(request, 'customer/chat.html')

def org_home(request):
    return render(request, 'orghome.html')


def register(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pin = request.POST.get('password')
        role = request.POST.get('role')

            
        print(username)
        print(email)
        print(role)

        #check if the email number is already registered
        if Account.objects.filter(phone_number=email).exists():
            print("phone number already registered")
            messages.info(request, f"Phone number already registered")
            return redirect('users:register')

    

        #     create a custom user with the phone number as the username and email backend as the password
        account = Account(
            phone_number = None,
            user_name = username,
            password=make_password(pin),
            email = email,
            role = role
        )
        
        
        account.save()
        messages.info(request, f"You are now registered as {username}")

        user = authenticate(request,username=email,password=pin)
        login(request,account)

        if user.is_authenticated:
            print("Authenticated")

        if role == "Organization":
            return redirect('users:org_home')

        if role == "Student":
            return redirect('users:customer_home')

        print("Authenticated")

    # except:
    #     return redirect('users:ptc-register')
    print("Done")

    return render(request,'register.html',data)

