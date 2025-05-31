from rest_framework import serializers
from .models import *


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class PostSerializers(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        queryset=group.objects.all(),
        slug_field='slug',
        required=False,
    )
    tag = TagSerializers(many=True)
    class Meta:
        model = Post
        fields = ('text', 'author', 'post_image', 'group', 'tag')

    def create(self, validated_data):
        if 'tag' not in self.initial_data:
            post = Post.objects.create()
            return post

        tag = validated_data.pop('tag')
        post = Post.objects.create(**validated_data)

        for tags in tag:
            current_tag, status = Tag.objects.get_or_create(
                **tags
            )
            PostTag.objects.create(
                tags=current_tag, post=post
            )
        return post

        

