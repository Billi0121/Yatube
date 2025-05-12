"""
URL configuration for yatube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    # path('/', views.index, name = 'index'),
    # path('auth/', views.not_authorizade, name = 'not_authorizade'),
    path('<str:username>', views.user_profile, name = 'user_profile'),
    path('group/<slug>/', views.group_post, name = 'group_post'),
     path('auth/', include('users.urls', namespace='users')),
    path('groupe/', views.groupe, name = 'group_list'),
    # path('auth/', include('django.contrib.auth.urls')),
    # path('/posts/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    path('new_book/', views.BookView.as_view(), name='new_book'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('post_create/', views.postview.as_view(), name='post_create'),
    path('<int:pk>/edit/', views.editview.as_view(), name = 'posts_edit'),
    path('about/', include('about.urls', namespace='about')),
    path('<int:pk>/posts/', views.users_post, name='users_post'),
    path('<int:pk>/post/', views.post_detail, name='post_detail'), 
    ]
handler404='core.views.page_not_found'
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )