from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from posts import *

# Create your views here.
def only_outhorizade(funn):
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, **args, **kwargs)
        return redirect('auth/login')
    return check_user

class me(TemplateView):
    template_name = 'about/me.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Hello'] = 'Nothing to say'
    
        return context


def technology(TemplateView):
    template_name = 'about/technology.html'
