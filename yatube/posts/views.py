from django.shortcuts import render
from posts.models import post

def index(request):
    posts = post.objects.order_by('-pub_date')[:10]
    context = {
        'postt': posts,
    }
    return render(request, 'posts/index.html', context)
def about(request):
    title = 'About Leve'
    context = {
        'title' : title
    }
    return render(request, 'posts/group_list.html', context)