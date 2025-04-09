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
        'signup/', views.SignUp.as_view(), name='signup'
        ),  
    path(
      'logout/',
      LoginView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
] 