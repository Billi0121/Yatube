from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    password = models.TextField()
    email = models.CharField(max_length=40)
    