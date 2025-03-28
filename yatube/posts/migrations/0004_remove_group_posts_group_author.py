# Generated by Django 5.1.7 on 2025-03-29 01:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_group'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='posts',
        ),
        migrations.AddField(
            model_name='group',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='authors_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
