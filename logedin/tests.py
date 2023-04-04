from django.test import TestCase
from . models import Team
from django.db import IntegrityError
import time
from users.models import CustomUser

# Create your tests here.

#test for the Team model
class TeamModelTest(TestCase):
    def setUp(self):
        #create an user named testuser
        self.user = CustomUser.objects.create_user(username="testuser", password="testpassword")

    def test_get_1000_teams_from_100000_teams(self):
        #create 100000 teams
        start = time.time()
        for i in range(100000):
            Team.objects.create(name="Team " + str(i), description="Team " + str(i) + " description", teamLeader=self.user)
        end = time.time()
        print("Time taken to create 100000 teams: " + str(end - start))
        #get current time
        start = time.time()
        #get 1000 teams        
        for i in range(41000, 42000):
            teams = Team.objects.get(pk=i)
        
        #get current time
        end = time.time()

        #print time taken
        print("Time taken to get 1000 teams from 1000000 teams: " + str(end - start))
