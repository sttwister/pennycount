from django.contrib.auth.models import User
from django.db import models

class GroupPayment(models.Model):
    user = models.ForeignKey(User, related_name='payments_added')
    title = models.CharField(max_length=2048)
    value = models.FloatField()
    shared_with = models.ManyToManyField(User, related_name='payments')

    def __unicode__(self):
        return self.title

class Payment(models.Model):
    group_payment = models.ForeignKey(GroupPayment)
    user = models.ForeignKey(User, related_name='')
    value = models.FloatField()

    def __unicode__(self):
        return '%s for %s' % (self.group_payment, self.user)

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends')
    friend = models.ForeignKey(User)
