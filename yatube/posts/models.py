from django.db import models
from django.contrib.auth import get_user_model
from .validators import *
from users.models import *

User = get_user_model()

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        "Group",  
        on_delete=models.SET_NULL,  
        blank=True, 
        null=True    
    )
    def __str__(self):
        return self.text

class group(models.Model):
    title = models.CharField(max_length=200, validators=[validate_not_empty])
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
        
class Book(models.Model):
    name = models.CharField(max_length=100, )
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField()
    
class Contact(models.Model):
    # К полю name подключаем валидатор, проверяющий, что поле не пустое.
    name = models.CharField(max_length=100, validators=[validate_not_empty])
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    # К полю body тоже подключаем валидатор, проверяющий, что поле не пустое.
    body = models.TextField()
    is_answered = models.BooleanField() 

