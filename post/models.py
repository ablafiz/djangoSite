from typing import ChainMap
from django.db import models
from django.conf import settings
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    other_field1= models.CharField(max_length=20) 
    other_field2= models.CharField(max_length=20) 
    other_field3= models.CharField(max_length=20) 
    other_field4= models.CharField(max_length=20) 
    other_field5= models.CharField(max_length=20) 
    other_field6= models.CharField(max_length=20) 
    other_field7= models.CharField(max_length=20) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text+ " " + str(self.created_date) +""+str(self.published_date)

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    createdon = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()
    
    def __str__(self):
        return self.firstname +" "+ self.middlename +" "+ self.lastname