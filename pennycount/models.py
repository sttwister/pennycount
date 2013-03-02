from django.contrib.auth.models import User
from django.db import models

class Payment(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=2048)
    value = models.FloatField()

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends')
    friend = models.ForeignKey(User)
