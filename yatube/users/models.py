from django.db import models
from django.contrib.auth import get_user_model




# Create your models here.

class UsersInFormation(models.Model):
    name = models.CharField()
    second_name = models.CharField()
    birth_year = models.DateField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        

    group = {
        'group',
        # on_delete=models.SETNULL
    }




class group(models.Model):
    slug = models.SlugField()
    about_slug = models.CharField()
    discription = models.TextField()