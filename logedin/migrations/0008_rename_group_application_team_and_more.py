# Generated by Django 4.1.7 on 2023-04-03 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logedin', '0007_alter_application_applicant_alter_membership_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='group',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='group',
            new_name='team',
        ),
    ]
