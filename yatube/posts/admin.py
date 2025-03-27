from django.contrib import admin
from posts.models import post

# Register your models here.
class Post_table(admin.ModelAdmin):
    list_display = ( 'pk','text', 'pub_date', 'author_id')
    search_fields = ('text',)
    list_filter = ('pub_date',)

admin.site.register(post, Post_table)
