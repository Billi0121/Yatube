from django.shortcuts import render, get_object_or_404, redirect
from posts.models import *
from django.contrib.auth.models import User
import datetime
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import *
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page




def authorized_only(func):
    """Cheking The if user authorizede"""
    def check_user(request, *args, **kwargs,):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')        
    return check_user

@cache_page(60)
@authorized_only
def index(request):
    """Menu"""
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        # 'postt': posts,
    }
    return render(request, 'posts/index.html', context, content_type='text/html', status=200)


@authorized_only
def indexx(request):
    """I doit it For Test"""
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
    """After Adding or Else Showing success Not to need it now"""
    return render(request, 'posts/thankyou.html')

class BookView(CreateView):
    """I created Him just for a Test""" 
    form_class = BookForm
    template_name = 'posts/books.html'  
    success_url = '/thankyou/' 

@authorized_only
def group_post(request, slug):
    """Going to groups Posts"""
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

def postview(request):
    """Creating Post"""
    user = User.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        # user.username = request.author
        form.save()
    return render(request, 'posts/post.html', {'form': form})

def post_edit(request, post_id):
    """Editing Post"""
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('post_detail', pk=post_id)

    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=post_id)
    context = {
        'post': post,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'posts/post.html', context) 


@authorized_only
def user_profile(request, username):
    """Show users Name in a main"""
    user_name = get_object_or_404(User, username=username)
    context = {
        'user_name': user_name
    }
    return render(request, 'posts/user_profile.html', context)

def users_post(request, pk):
    """Sorting Post by user"""
    User_pk = User.objects.get(pk=pk)
    user_post = Post.objects.filter(author=User_pk)
    paginator = Paginator(user_post, 5)
    page_count = request.GET.get('page')
    result_paginator = paginator.get_page(page_count)
    context = {
        'page_obj': result_paginator
    }
    return render(request, 'posts/user_posts.html', context)

@authorized_only
def post_detail(request, pk):
    """Showing Posts detail EX likes Comments"""
    post = Post.objects.get(pk=pk)
    comments = comment.objects.filter(post_id=pk)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'posts/post_detail.html', context)

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect('post_detail', pk=post_id)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'posts/addcomment.html', context)