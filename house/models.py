from typing import ChainMap
from django.db import models
from django.conf import settings
from django.db.models.expressions import Window
from django.db.models.fields import CharField
from django.utils import timezone

class House(models.Model):
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    ward = models.CharField(max_length=20)
    vilage = models.CharField(max_length=20)
    strit = models.CharField(max_length=20)

    def saveme(self):
        self.save()
    
    def __str__(self):
        return "The house is located at "+ self.region+" Region"