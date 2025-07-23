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

# @cache_page(10)
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


# @authorized_only
# def indexx(request):
#     """I doit it For Test"""
#     author = User.objects.get(username='leo')
#     keywoard = 'утро'
#     start_date = datetime.date(1854, 7, 7)
#     end_date = datetime.date(1854, 7, 21)
#     posts = Post.objects.filter(text__contains=keywoard).filter(author=author).filter(pub_date__range=(start_date, end_date))
#     context = {
#         'group': group,
#         'postt': posts,
#     }
#     return render(request, 'posts/index.html', context)

@authorized_only
def thankyou(request):
    """After Adding or Else Showing success Not to need it now"""
    return render(request, 'posts/thankyou.html')


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
    form_post = PostForm(
        request.POST or None,
        files=request.FILES or None,)
    if form_post.is_valid():
        Post = form_post.save(commit=False)
        Post.author = request.user
        form_post.save()
        return redirect('index')
    return render(request, 'posts/post.html', {'form': form_post})

def following(request, username):
    user = User.objects.get(username=username)
    form = FollowersForm(request.POST or None)
    if form.is_valid():
        form =  form.save(commit=False)
        Followers.user = user   
        Followers.following = request.user
        form.save()
    context = {
        'form': form
    }
    return render(request, 'posts/index.html', context)


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
    return render(request, 'posts/post_detail.html', context)

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
    # check = Followers.objects.get(following=user_name.id)
    # followersform =FollowersForm(request.POST or None)
    # if followersform.is_valid():
    #     Followerss = followersform.save(commit=False)
    #     Followerss.user = request.user
    #     Followerss.following = user_name
    #     Followerss.save()
    #     followersform = FollowersForm()
    # user = request.user
    context = {
        'user_name': user_name,
        # 'check': check,
        # 'user': user
    }
    return render(request, 'posts/user_profile.html', context)

@authorized_only
def users_post(request, pk):
    """Sorting Post by user"""
    User_pk = User.objects.get(pk=pk)
    post_count = Post.objects.filter(author=User_pk).count()
    user_post = Post.objects.filter(author=User_pk)
    paginator = Paginator(user_post, 5)
    page_count = request.GET.get('page')
    result_paginator = paginator.get_page(page_count)
    context = {
        'page_obj': result_paginator,
        'post_count': post_count
    }
    return render(request, 'posts/index.html', context)

@authorized_only
def post_detail(request, pk):
    """Showing Posts detail EX likes Comments"""
    post = Post.objects.get(pk=pk)
    post_count = Post.objects.filter(author=post.author).count()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.author = request.user
        new_comment.post = post
        new_comment.save()
        form = CommentForm()
    comments = comment.objects.filter(post_id=pk)
    # followers = Followers.objects.all()
    context = {
        # 'cheking': followers,
        # 'followersform': followersform,
        'post_count': post_count,
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/post_detail.html', context)


@authorized_only
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('index')
    return render(request, 'posts/delete.html')

def send_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {email}\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['billibi0121@gmail.com'],  # 👉 замени на свою почту
            )
            return render(request, 'posts/index.html')
    else:
        form = ComplaintForm()
    return render(request, 'posts/complaint_form.html', {'form': form})

# class post_api(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class post_api_edit(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#Tnasfering
# Hello
from rest_framework.decorators import api_view, action
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions, throttling
from .permissions import *
from .throttling import *
from rest_framework.throttling import ScopedRateThrottle
from .pagination import *
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (AuthorOrReadOnly,)
    throttle_classes = (LunchBrakeThrolling, ScopedRateThrottle)
    throttle_scope = 'low_request'
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$text',)# Regex $ learn in documentation later


    # @action(detail=False, url_path='white-cats')
    # def white_cat(self, request):
    #     new = Post.objects.filter(author=2)
    #     serializer = self.get_serializer(new)
    #     return Response(serializer.data)

    def perform_create(self, serializers):
        return serializers.save(author=self.request.user)
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        else:
            return super().get_permissions()
        
    # @action(detail=False, url_path='BG')
    # def bg(self, request):
    #     post = Post.objects.get(id=3)
    #     serializer = self.get_serializer(post)
    #     return Response(serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = group.objects.all()
    serializer_class = GroupSerializers

from django.core.mail import send_mail
from django.conf import settings