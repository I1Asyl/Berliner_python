# Generated by Django 4.1.7 on 2023-04-16 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logedin', '0019_post_date_post_parentpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parentpost',
        ),
    ]
