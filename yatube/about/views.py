from django.shortcuts import render, redirect
# from django.urls import 
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from posts import *

# def only_user_log(func):
#     def check_user(request, **kwargs):
#         if request.user.is_authenticated:
#             return render(request, **kwargs)
#         return redirect('/auth/login/')
#     return check_user



class me(TemplateView):
    template_name = 'about/me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Hello'] = 'Nothing to say'
        context['Me'] = User.objects.get(pk=1)
    
        return context


def technology(TemplateView):
    template_name = 'about/technology.html'
