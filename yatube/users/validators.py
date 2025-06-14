from django import forms

def validate_not_empty(name):
    if name == '':
        raise forms.ValidationError(
            'А кто поле будет заполнять, Пушкин?',
            params={'name': name},
        )  