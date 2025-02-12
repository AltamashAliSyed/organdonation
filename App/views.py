from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Hospital,Donor
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


def home(request):
    return render(request,'home.html')

#def search_data(request):
    query = request.GET.get('query','').lower()
    response = "I cna help you to find Hospital and donors"

    if "hospital"in query:
        hospitals = Hospital.objects.all().values('hospital_name','hospital_address','hospital_phonenumber')
        response = list(hospitals) if hospitals else "No hospitals Found"

    elif "donor" in query:
        donors = Donor.objects.all().values('name','blood_grp','city', 'contact_number')
        response = list(donors) if donors else "No donors Found"

    return JsonResponse({'message':response})





def Hospital_view(request):
    hospital = Hospital.objects.all()
    return render(request, 'hospital.html',{'hospital': hospital})  

def Donor_view(request):
    donors = Donor.objects.all()
    return render(request,'donors.html',{'donors':donors})


@custom_login
def hospital_form(request):
    if request.method == "POST":
        hospital_name = request.POST.get("hospital_name")
        hospital_address = request.POST.get("hospital_Address")
        hospital_phonenumber = request.POST.get("hospital_phonenumber")

        
        Hospital.objects.create(
            hospital_name=hospital_name,
            hospital_address=hospital_address,  
            hospital_phonenumber=hospital_phonenumber
        )
        return redirect("hospital")  

    return render(request, "hospitalform.html")
@custom_login
def donor_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        age = request.POST.get("age")
        blood_grp = request.POST.get("blood_grp")
        organ_name = request.POST.get("organ_name")
        city=request.POST.get("city")
        contact_number=request.POST.get("contact_number")

        
        Donor.objects.create(
            name = name,
            address = address,
            age = age,
            blood_grp =blood_grp,
            organ_name = organ_name,
            city=city,
            contact_number=contact_number,

        )
        return redirect("donor")  

    return render(request, "donorform.html")