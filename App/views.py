from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
from .decorators import custom_login

def Signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')  

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists!')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registered successfully!")
            return redirect('login')

    return render(request, 'signup.html')

@custom_login         
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username and password')

    return render(request,'login.html')

@custom_login
def logout_view(request):
    logout(request)
    messages.success(request,'Logout Succesfull')
    return redirect('login')

@custom_login
def home(request):
    return render(request,'home.html')



def Hospital(request):
    pass

def Donor(request):
    pass