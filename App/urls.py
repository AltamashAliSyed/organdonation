from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.Signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.home,name='home'),
    path('donors/',views.Donor_view,name='donor'),
    path('hospital/',views.Hospital_view,name='hospital'),
    path('hospital_form/',views.hospital_form,name='hospital_form'),
    path('donor_form/',views.donor_form,name='donor_form'),
   

]
