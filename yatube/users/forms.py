from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from .validators import *
from django import forms
 
User = get_user_model()




class SignUpForm(UserCreationForm):
    # Правильно определяем поля формы — ВНЕ Meta!
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
