# Generated by Django 2.2.4 on 2019-08-31 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
