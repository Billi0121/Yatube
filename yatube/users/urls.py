from django.contrib.auth.views import *
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
        'signup/', views.SignUpView.as_view(), name='signup'
        ),  
    path(
      'logout/',
      views.logout_view,
      name='logged_out'
    ),
    path(
      'password_reset_form/',
      LoginView.as_view(template_name='users/password_reset_form.html'),
      name='password_reset_form'
    ),
    path(
      'password_change_form/',
      PasswordChangeView.as_view(template_name='users/password_change_form.html'),
      name='password_change_form'
    ),
    path(
      'password_change_done/',
      PasswordResetDoneView.as_view(template_name='users/password_change_done.html'),
      name='password_change_done'
    ),
    path(
      'password_reset/done/',
      PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
      name='password_reset_done'
    ),
    path(
      'password_reset_form/',
      PasswordResetView.as_view(template_name='users/password_reset_form.html'),
      name='password_reset_form'
    ),
] 
