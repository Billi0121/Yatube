from django.db import models
from django.contrib.auth import get_user_model
from .validators import *
from users.models import *
from pytils.translit import slugify

User = get_user_model()


class Tag(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
# Create your models here.
class Post(models.Model):
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

    tagpost = models.ManyToManyField(Tag, through='PostTag')

    def __str__(self):
        return self.text

class PostTag(models.Model):
    tag = models.ForeignKey(Tag, on_dleete=models.CASCADE)
    post = models.ForiegnKey(Post, on_delete=models.CASCADE)

class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class group(models.Model):
    title = models.CharField(max_length=200, validators=[validate_not_empty])
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
        
class Book(models.Model):
    name = models.CharField(max_length=100,)
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField()
    image = models.ImageField(
        'Картинка',
        upload_to='yatube/',
        blank=False,
        null=False,
        help_text='Загрузите картинку'
    )

    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    # К полю name подключаем валидатор, проверяющий, что поле не пустое.
    name = models.CharField(max_length=100, validators=[validate_not_empty])
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    # К полю body тоже подключаем валидатор, проверяющий, что поле не пустое.
    body = models.TextField()
    is_answered = models.BooleanField() 


def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)[:100]
    super().save(*args, **kwargs)
