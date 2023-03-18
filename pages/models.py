from django.db import models

class Group(models.Model):
    groupName = models.CharField(max_length=50, default='unnamed group')
    groupSize = models.IntegerField(default=1)
    #groupOwner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.groupName
# Create your models here.
