from django.shortcuts import redirect
from django.urls import reverse

def custom_login(view_func):
    def wrap_view(request, *args, **kwargs):
        
        if not request.user.is_authenticated:
            
            if request.path != reverse('login'): 
                return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrap_view
