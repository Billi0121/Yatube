from django.contrib.auth.views import LoginView 
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path(
      'login/',
      LoginView.as_view(template_name='users/login.html'),
      name='login'
    ),
    path(
      'signup/',
      LoginView.as_view(template_name='users/signup.html'),
      name='signup'
    ),
    path(
      'logout/',
      LoginView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
] 