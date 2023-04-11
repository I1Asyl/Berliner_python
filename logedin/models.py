from django.db import models
from users.models import CustomUser

#create your models here.
#models.Model is a class that is inherited by all models

#model called Team
class Team(models.Model):
    #teamLeader is a foreign key to the CustomUser model
    teamLeader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="createdTeams", related_query_name="createdTeam", to_field='username')

    #members is a many to many field to the CustomUser model for team members through the Membership model
    members = models.ManyToManyField(CustomUser, through='Membership', through_fields=('team', 'member'), related_name="memberTeams", related_query_name="memberTeam")
    
    #applications is a many to many field to the CustomUser model for applicants through the Application model
    applicants = models.ManyToManyField(CustomUser, through='Application', through_fields=('team', 'applicant'))

    #name and description of the team    
    name = models.CharField(default="New team", max_length=30, unique=True)
    description = models.CharField(default="Recently created team", max_length=60)

class Application(models.Model):
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    comment = models.CharField(default="", max_length=200)
    def __str__(self) -> str:
        return self.applicant.username + " applied to " + self.team.name

class Membership(models.Model):
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    #isLeader is a boolean field that is true if the member is the team leader
    isLeader = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.member.username + " is in " + self.team.name + " isLeader: " + str(self.isLeader)

class Posts(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.author.username + " posted in " + self.team.name + ": " + self.content