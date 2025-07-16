from django import forms
from .models import *


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
        fields = ['title', 'text', 'group', 'post_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['text']

class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        fields = ['user', 'following']
    

class ComplaintForm(forms.Form):
    email = forms.EmailField(label="Your Email")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
