# Generated by Django 4.1.7 on 2023-04-13 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logedin', '0015_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamLeader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdTeams', related_query_name='createdTeam', to=settings.AUTH_USER_MODEL),
        ),
    ]