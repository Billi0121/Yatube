from django.contrib import admin
from posts.models import Post, group, Book
from users.models import Users

# Register your models here.
class Post_table(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-' 

class Book_table(admin.ModelAdmin):
    list_display= (
        'name',
        'isbn',
    )
    list_filter = ('name',)

admin.site.register(Users)
admin.site.register(Book, Book_table)
admin.site.register(group)
admin.site.register(Post, Post_table)
