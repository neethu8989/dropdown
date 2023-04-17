from django.db import models

# Create your models here.
from django.db import models


class Districts(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branches(models.Model):
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):

    district = models.ForeignKey(Districts, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, blank=True, null=True)

