# Generated by Django 4.2.3 on 2024-01-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
