# Generated by Django 5.1.7 on 2025-03-29 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_group_posts_group_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='author',
            new_name='post',
        ),
    ]
