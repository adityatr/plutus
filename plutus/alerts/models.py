from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alerts(models.Model):
    primary_key = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=30)
    due = models.DateField(max_length=30)

