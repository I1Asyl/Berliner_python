# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django import forms

class CustomUser(AbstractUser):
    birthDate = models.DateTimeField(null=True)
    class Meta:
        pass
