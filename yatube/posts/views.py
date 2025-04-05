from django.shortcuts import render, get_object_or_404
from posts.models import Post, group
from django.contrib.auth.models import User
import datetime


def index(request):
    posts = Post.objects.all()
    context = {
        'postt': posts,
    }
    return render(request, 'posts/index.html', context)

def group(request):
    title = 'Empty'
    post_objects = Post.objects.all()
    context = {
        'title': title,
    }
    return render(request, 'posts/group.html', context)

def indexx(request):
    author = User.objects.get(username='leo')
    keywoard = 'утро'
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)
    posts = Post.objects.filter(text__contains=keywoard).filter(author=author).filter(pub_date__range=(start_date, end_date))
    context = {
        'group': group,
        'postt': posts,
    }
    return render(request, 'posts/index.html', context)


def group_post(request, slug):
    Group = get_object_or_404(group, slug=slug)
    posts = Post.objects.filter(group=Group).order_by('-pub_date')[:10]
    context = {
        'Group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


