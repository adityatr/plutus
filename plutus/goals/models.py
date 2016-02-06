from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goals(models.Model):
    primary_key = models.ForeignKey(User, on_delete=models.CASCADE)
    current = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    max_amount = models.DecimalField(default=0, decimal_places=2, max_digits=20)
    duration = models.CharField(default=0, max_length=10)

    
