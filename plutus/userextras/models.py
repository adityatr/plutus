from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_location_info(models.Model):
    primary_key = models.ForeignKey(User,on_delete=models.CASCADE)
    street_no = models.IntegerField(default=0)
    street = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
        
class user_personal_info(models.Model):
    age = models.IntegerField(default=0)
    goals = models.CharField(max_length=10)
    alerts = models.CharField(max_length=10)
    communities = models.CharField(max_length=10)
    accounts = models.CharField(max_length=10)
    bills = models.CharField(max_length=10)
    budget = models.CharField(max_length=10)
    spending = models.CharField(max_length=10)
    income = models.CharField(max_length=10)
    friends = models.CharField(max_length=10)
    messages = models.CharField(max_length=10)
    achievements = models.CharField(max_length=10)




    
