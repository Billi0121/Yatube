from posts.models import *
from django.shortcuts import get_object_or_404
from django.db.models import Max, Min, Sum, Count

def group_post(request, slug):
    Group = get_object_or_404(group, slug=slug)
    posts = Post.objects.filter(group=Group).order_by('-pub_date')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'slug': slug,
        'Group': group,
        # 'posts': posts,
        'obj': page_obj,
    }
    return render(request, 'posts/group_post.html', context)    
   
    
