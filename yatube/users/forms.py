from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from .validators import *
from django import forms
 
User = get_user_model()




class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        email = forms.CharField(max_length=30)
        first_name = forms.CharField(max_length=30)
        last_name = forms.CharField(max_length=30)
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]
        email = forms.CharField(max_length=30)
