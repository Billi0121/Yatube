from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, group
from django.contrib.auth.models import User
import datetime
from django.views.generic.edit import CreateView
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import *


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

def test(request):
    # Создаём объект формы
    form = ContactForm()

    # И в словаре контекста передаём эту форму в HTML-шаблон
    return render(request, 'users/test.html', {'form': form}) 


class postview(CreateView):
    form_class = PostForm
    template_name = 'posts/post.html'
    success_url = '/thankyou/'

# def postview(request):
#     form = PostForm()
#     form_class = PostForm
#     context = {
#         'form': form
#     }
#     return render(request, 'posts/post.html', context)

def test(request):
    return render(request, 'posts/test.html')

@authorized_only
def user_profile(request, username):
    user_name = get_object_or_404(User, username=username)
    context = {
        'user_name': user_name
    }
    return render(request, 'posts/user_profile.html', context)