from django import forms

def validate_not_empty(title):
    # Проверка "а заполнено ли поле?"
    if title == '':
        raise forms.ValidationError(
            'А кто поле будет заполнять, Пушкин?',
            params={'title': title},
        )  