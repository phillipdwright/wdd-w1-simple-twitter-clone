from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    # Add our fields here
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Tweet(models.Model):
    # Add our fields here
    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)