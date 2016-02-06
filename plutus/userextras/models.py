from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Extra(models.Model):
    primary_key = models.ForeignKey(User, on_delete=models.CASCADE)

    age = models.IntegerField(default=0)

    street_no = models.IntegerField(default=0)
    street = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    spending = models.IntegerField(default=0)
    income = models.IntegerField(default=0)


