from django.contrib import admin
from .models import *

# Register your models here.

class UserinformationsForm(admin.ModelAdmin):
    list_display = ['name', 'second_name', 'birth_year' ]


admin.site.register(UsersInformation, UserinformationsForm)
admin.site.register(group)