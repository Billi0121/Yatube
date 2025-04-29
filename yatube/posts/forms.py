from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'isbn', 'pages') 

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=100)
#     body = forms.CharField(widget=forms.Textarea)
#     is_answered = forms.BooleanField()

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'body', 'is_answered']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text','group']