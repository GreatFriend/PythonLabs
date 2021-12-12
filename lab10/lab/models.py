from django.db import models


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    access=models.IntegerField(default=0)

class Citizen(models.Model):
    name = models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    place_reg = models.CharField(max_length=200)
