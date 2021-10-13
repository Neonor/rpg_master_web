'''
Created on 12 oct. 2021

@author: neonor
'''
from django.conf import settings
from django.db import models as m
from django.contrib.auth.models import User

class Group(m.Model):
    NAME=m.CharField(max_length=50)
    # PERMISSIONS=m.JSONField(default=[])

class GroupUser(m.Model):
    GROUP=Group()
    USER=User()
    ADMIN=m.BooleanField(default=False)
    