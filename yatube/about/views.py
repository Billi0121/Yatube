from django.shortcuts import render

# Create your views here.
def me(request):
    return render(request, 'about/me.html')

def technology(request):
    return render(request, 'about/technology.html')