from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Friend(models.Model):
    me = models.ForeignKey(User, on_delete=models.CASCADE)
    
    friend_id = models.CharField(max_length=30)
    

class Communities(models.Model):
    primary_key = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    member = models.CharField(max_length=30)
    posts = models.IntegerField(default=0)
    
class Message(models.Model):
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    
    from_id = models.CharField(max_length=30)
    
    message = models.CharField(max_length=1000)
    
class Achievments(models.Model):
    primary_key = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=30)
    points = models.IntegerField(default=0)