# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django import forms

class CustomManager(models.Manager):
    def get_queryset(self):
        arra = []
        arra.append(super(CustomManager, self).get_queryset().all())
        return arra
class CustomUser(AbstractUser):
	birthDate = models.DateTimeField(null=True)
	objects = models.Manager()
	customManager = CustomManager()
	class customMeta():
		home = 'home'