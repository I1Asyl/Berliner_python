# Generated by Django 4.1.7 on 2023-04-03 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logedin', '0010_membership_is_leader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='is_leader',
            new_name='isLeader',
        ),
    ]