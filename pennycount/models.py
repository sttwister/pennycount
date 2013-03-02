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

class Payment(models.Model):
    group_payment = models.ForeignKey(GroupPayment)
    user = models.ForeignKey(User, related_name='')
    value = models.FloatField()

    def __unicode__(self):
        return '%s for %s' % (self.group_payment, self.user)

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends')
    friend = models.ForeignKey(User)

@receiver(post_save, sender=GroupPayment)
def group_payment_post_save(sender, instance, created, raw, **kwargs):
    print instance, created, raw
    # Model is newly created, but not from fixture
    if created and not raw:
        user_count = instance.shared_with.count()
        for user in instance.shared_with.all():
            payment = Payment()
            payment.group_payment = instance
            payment.user = user
            payment.value = group_payment.value / user_count
            payment.save()
