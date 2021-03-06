# Generated by Django 3.0.3 on 2020-03-30 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_published',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
    ]
