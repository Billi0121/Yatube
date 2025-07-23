from django.shortcuts import render
# from django.views.generic.edit import CreateView, 
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import logout
from django.shortcuts import redirect



def page_not_found(request, exception):
    return render(request, 'users/signup.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

def admin_detail(request):
    return render(request, 'users/logout.html')

def users(request):
    return render(request, 'users/logout.html')

class SignUpView(CreateView):
        form_class = SignUpForm 
        template_name = 'users/signup.html'
        success_url = reverse_lazy('thankyou')



