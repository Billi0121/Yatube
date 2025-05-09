from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()
# Create your models here.

class UsersInformation(models.Model):
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    birth_year = models.DateField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
        

    group = models.ForeignKey(
        'group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )




class group(models.Model):
    slug = models.SlugField()
    about_slug = models.CharField(max_length=20)
    discription = models.TextField()

    def __str__(self):
        return self.slug