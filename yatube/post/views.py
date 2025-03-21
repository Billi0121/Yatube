from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'post/index.html' )


def about(request):
    context = {
        'title': 'About sites',
        'year': date.today(),
    }
    return render(request, 'post/group_list.html', context)