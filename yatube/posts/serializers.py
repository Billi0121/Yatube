from rest_framework import serializers
from .models import *


class GroupSerializers(serializers.ModelSerializer):
    class meta:
        model = group
        fields = ['slug']

class PostSerializers(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        queryset=group.objects.all(),
        slug_field='slug',
        required=False,
    )
    class Meta:
        model = Post
        fields = ('text', 'author', 'post_image', 'group')