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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[validate_not_empty])
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    is_answered = forms.BooleanField()