# Generated by Django 3.2.5 on 2021-07-19 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startpost',
            old_name='StoryPostAuthor',
            new_name='StartPostAuthor',
        ),
        migrations.RenameField(
            model_name='startpost',
            old_name='StoryPostBody',
            new_name='StartPostBody',
        ),
        migrations.RenameField(
            model_name='startpost',
            old_name='StoryPostBodyImage',
            new_name='StartPostBodyImage',
        ),
        migrations.RenameField(
            model_name='startpost',
            old_name='StoryPostTime',
            new_name='StartPostTime',
        ),
    ]
