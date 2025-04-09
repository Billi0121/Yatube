# Generated by Django 5.1.7 on 2025-04-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='second_name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
