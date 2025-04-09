from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm# from django.user import get_user_model_or_404


def admin_detail(request):
    return render(request, 'users/logout.html')

def users(request):
    return render(request, 'users/logout.html')


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'