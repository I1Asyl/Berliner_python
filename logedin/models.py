from django.db import models
from users.models import CustomUser

class Team(models.Model):
    teamLeader = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="createdTeams", related_query_name="createdTeam", null=True, to_field='username', blank=True)
    members = models.ManyToManyField(CustomUser, through='Membership', through_fields=('group', 'member'))
    name = models.CharField(default="New team", max_length=30, unique=True)
    description = models.CharField(default="Recently created team", max_length=60)

class Membership(models.Model):
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Team, on_delete=models.CASCADE)

