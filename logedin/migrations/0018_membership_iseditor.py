# Generated by Django 4.1.7 on 2023-04-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logedin', '0017_post_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='isEditor',
            field=models.BooleanField(default=False),
        ),
    ]
