from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView


def admin_detail(request):
    return render(request, 'users/logout.html')

def users(request):
    return render(request, 'users/logout.html')

# class SignUp(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('thankyou')
#     template_name = 'users/signup.html'

class SignUpView(CreateView):
        form_class = SignUpForm 
        template_name = 'users/signup.html'
        success_url = reverse_lazy('thankyou')




