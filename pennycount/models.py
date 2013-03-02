from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class GroupPayment(models.Model):
    user = models.ForeignKey(User, related_name='payments_added')
    title = models.CharField(max_length=2048)
    value = models.FloatField()
    shared_with = models.ManyToManyField(User, related_name='payments')

    def __unicode__(self):
        return self.title

    def create_payments(self):
        user_count = self.shared_with.count()
        for user in self.shared_with.all():
            payment = Payment()
            payment.group_payment = self
            payment.user = user
            payment.value = self.value / user_count
            payment.save()

class Payment(models.Model):
    group_payment = models.ForeignKey(GroupPayment)
    user = models.ForeignKey(User, related_name='')
    value = models.FloatField()

    def __unicode__(self):
        return '%s for %s' % (self.group_payment, self.user)

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends')
    friend = models.ForeignKey(User)
