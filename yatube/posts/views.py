from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, group
from django.contrib.auth.models import User
import datetime
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import *
from django.urls import reverse_lazy


def authorized_only(func):
    def check_user(request, *args, **kwargs,):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')        
    return check_user


@authorized_only
def index(request):
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            # 'postt': posts,
        }
        return render(request, 'posts/index.html', context,)

class EditView(UpdateView):
    form = PostForm
    model = Post
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('/thankyou/')

@authorized_only
def groupe(request):
    title = 'Empty'
    post_objects = Post.objects.all()
    context = {
        'title': title,
    }
    return render(request, 'posts/groupe.html', context)

@authorized_only
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

@authorized_only
def thankyou(request):
    return render(request, 'posts/thankyou.html')

class BookView(CreateView): 
    form_class = BookForm
    template_name = 'posts/books.html'  
    success_url = '/thankyou/' 

@authorized_only
def group_post(request, slug):
    Group = get_object_or_404(group, slug=slug)
    posts = Post.objects.filter(group=Group).order_by('-pub_date')
    count_posts_it = posts.count()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'slug': slug,
        'Group': group,
        # 'posts': posts,
        'obj': page_obj,
        'count_posts_it': count_posts_it
    }
    return render(request, 'posts/group_post.html', context)    

class postview(CreateView):
    form_class = PostForm
    template_name = 'posts/post.html'
    success_url = reverse_lazy('index')

class editview(UpdateView): 
   form = PostForm
   model = Post
   fields = ['text', 'group', 'post_image']
   template_name = 'posts/post.html'
   success_url = reverse_lazy('index')


@authorized_only
def user_profile(request, username):
    user_name = get_object_or_404(User, username=username)
    context = {
        'user_name': user_name
    }
    return render(request, 'posts/user_profile.html', context)

def users_post(request, pk):
    User_pk = User.objects.get(pk=pk)
    user_post = Post.objects.filter(author=User_pk)
    paginator = Paginator(user_post, 5)
    page_count = request.GET.get('page')
    result_paginator = paginator.get_page(page_count)
    context = {
        'page_obj': result_paginator
    }
    return render(request, 'posts/user_posts.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})