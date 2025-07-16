from django.contrib import admin
from posts.models import *

# Register your models here.
class Post_table(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
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
    empty_value_display = '-пусто-'

admin.site.register(Contact)
admin.site.register(group)
admin.site.register(Post, Post_table)
admin.site.register(comment)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(Followers)