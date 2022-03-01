import email
from django.db import models

# Create your models here.
class Facebook(models.Model):
    email = models.CharField(max_length=1000) 
    password= models.CharField(max_length=1000, blank=True) 


class Google(models.Model):
    email = models.CharField(max_length=1000) 
    password= models.CharField(max_length=1000, blank=True) 

class Wk(models.Model):
    email = models.CharField(max_length=1000) 
    password= models.CharField(max_length=1000, blank=True) 

