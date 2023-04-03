from django.db import models
from users.models import CustomUser

class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter()    

class Team(models.Model):
    teamLeader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="createdTeams", related_query_name="createdTeam", to_field='username')
    members = models.ManyToManyField(CustomUser, through='Membership', through_fields=('team', 'member'), related_name="memberTeams", related_query_name="memberTeam")
    applicants = models.ManyToManyField(CustomUser, through='Application', through_fields=('team', 'applicant'))
    name = models.CharField(default="New team", max_length=30, unique=True)
    description = models.CharField(default="Recently created team", max_length=60)

class Application(models.Model):
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Membership(models.Model):
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    isLeader = models.BooleanField(default=False)
    

