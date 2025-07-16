from posts.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Max, Min, Sum, Count

def user_profile(request, username):
    user_name = get_object_or_404(User, username=username)
    context = {
        'user_name': user_name
    }
    # return render(request, 'posts/user_profile.html', context)
   
    
