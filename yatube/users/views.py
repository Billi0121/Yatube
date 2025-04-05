from django.shortcuts import render
# from django.user import get_user_model_or_404
# Create your views here.

def admin_detail(request):
    return render(request, 'users/logout.html')

def users(request):
    return render(request, 'users/logout.html')