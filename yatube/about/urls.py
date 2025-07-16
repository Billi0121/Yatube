from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('me/', views.me.as_view(), name='me'),
    path('technology/', views.technology, name='technology'),
]
