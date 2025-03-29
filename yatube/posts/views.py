from django.shortcuts import render, get_object_or_404
from posts.models import Post, group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'postt': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request,):
    # group = get_object_or_404(Group, slug=post_slug)
    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # context = {
    #     'group': group,
    #     'posts': posts,
    # }
    return render(request, 'posts/group_list.html/') 

