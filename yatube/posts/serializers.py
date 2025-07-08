from rest_framework import serializers
from .models import *
import datetime

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = group
        fields = ['title', 'slug', 'description']

class PostSerializers(serializers.ModelSerializer):
    tag = TagSerializers(many=True, required=False)
    character_quantity = serializers.SerializerMethodField()
    publication_date = serializers.DateTimeField(source='pub_date', read_only=True)
    group = serializers.SlugRelatedField(
        queryset=group.objects.all(),
        slug_field='slug',
        required=False,
    )
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', 'post_image', 'group', 'tag','character_quantity', 'publication_date')
        read_only_fields = ('author',)
        
    def create(self, validated_data):
        if 'tag' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post

        tag = validated_data.pop("tag")
        post = Post.objects.create(**validated_data)

        for tags in tag:
            current_tag, status = Tag.objects.get_or_create(
                **tags
            )
            PostTag.objects.create(
                tags=current_tag, post=post
            )
        return post

    def get_character_quantity(self, obj):
        return len(obj.text)