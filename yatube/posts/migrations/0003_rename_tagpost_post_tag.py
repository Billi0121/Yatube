# Generated by Django 5.1.7 on 2025-05-30 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tag_posttag_post_tagpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tagpost',
            new_name='tag',
        ),
    ]
