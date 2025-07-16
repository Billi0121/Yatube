from django.db import models
from django.contrib.auth import get_user_model
from .validators import *
from users.models import *
from pytils.translit import slugify

User = get_user_model()


class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',blank=True, null=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following',blank=True, null=True)#blank=True, null=True
    
    def __str__(self):
        return f'{self.user} {self.following}'

class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(
        'Img',
        upload_to='yatube/',
        blank=True,
        null=True,
        help_text='Upload your image if you want'
    )
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
    tag = models.ManyToManyField(Tag, through='PostTag')

    def __str__(self):
        return self.text    


class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text


class group(models.Model):
    title = models.CharField(max_length=200,)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class PostTag(models.Model):
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Tag:{self.tags}  Post:{self.post}'

  
class Contact(models.Model):
    # К полю name подключаем валидатор, проверяющий, что поле не пустое.
    name = models.CharField(max_length=100, validators=[validate_not_empty])
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    # К полю body тоже подключаем валидатор, проверяющий, что поле не пустое.
    body = models.TextField()
    is_answered = models.BooleanField() 
