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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('group/<slug>/', views.group_post, name = 'user_about'),
     path('auth/', include('users.urls', namespace='users')),
    path('groupe/', views.groupe, name = 'group_list'),
    # path('auth/', include('django.contrib.auth.urls')),
    path('new_book/', views.BookView.as_view(), name='new_book'),
    path('thankyou/', views.thankyou, name='thankyou')
    ]

