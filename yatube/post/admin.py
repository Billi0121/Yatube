from django.contrib import admin
from post.models import Post

# Register your models here.
class AdminPost(admin.ModelAdmin):
     # Перечисляем поля, которые должны отображаться в админке
    list_display = ('text', 'pub_date', 'author') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    avaible_list_value = 'Pusto'

admin.site.register(Post, AdminPost)