# Generated by Django 5.1.7 on 2025-04-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
