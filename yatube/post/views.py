from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    context = {
        'text': 'There\nis no one\nwho can create\nsomething witout me',
    }
    return render(request, 'post/index.html', context)


def about(request):
    context = {
        'text': 'There is no one who can create something witout me',
        'title': 'About sites',
        'year': date.today(),
    }
    return render(request, 'post/group_list.html', context)