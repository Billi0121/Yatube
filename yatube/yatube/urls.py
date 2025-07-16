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
from rest_framework.routers import SimpleRouter, DefaultRouter
from posts.views import *

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('post_create/', views.postview, name='post_create'),
    # path('/', views.index, name = 'index'),
    # path('auth/', views.not_authorizade, name = 'not_authorizade'),
    path('profile/<str:username>/', views.user_profile, name = 'user_profile'),
    path('group/<slug>/', views.group_post, name = 'group_post'),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/v1/', include('djoser.urls')),
    path('auth/v1/', include('djoser.urls.jwt')),
    path('follwing/<str:username>/', views.following, name='following'),
    # path('auth/', include('django.contrib.auth.urls')),
    # path('/posts/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('<int:post_id>/edit/', views.post_edit, name = 'posts_edit'),
    path('about/', include('about.urls', namespace='about')),
    path('<int:pk>/posts/', views.users_post, name='users_post'),
    path('<int:pk>/post_detail/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    # path('api/v1/posts/' , views.post_api.as_view()),
    # path('api/v1/posts/<int:pk>/', views.post_api_edit.as_view())
    path('support/', views.send_complaint, name='send_complaint'),
    # path('subscribe/<int:pk>/', views.subscribe, name='subscribe'),
    ]
# handler404='users.views.page_not_found'
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),) 
