from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    name = models.CharField(default="", max_length=20)
    surname = models.CharField(default="", max_length=20)