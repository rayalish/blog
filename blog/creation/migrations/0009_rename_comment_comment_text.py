# Generated by Django 4.2.3 on 2024-01-13 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0008_rename_movie_comment_blog_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
    ]
