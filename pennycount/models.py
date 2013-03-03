from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

class GroupPayment(models.Model):
    user = models.ForeignKey(User, related_name='payments_added')
    title = models.CharField(max_length=2048)
    value = models.FloatField()
    shared_with = models.ManyToManyField(User, related_name='group_payments')
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def create_payments(self):
        user_count = self.shared_with.count()
        for user in self.shared_with.all():
            if self.user != user:
                payment = Payment()
                payment.group_payment = self
                payment.user = user
                payment.value = float(self.value) / user_count
                payment.save()
                payment.send_email()

class Group(models.Model):
    user = models.ForeignKey(User, related_name='my_groups')
    users = models.ManyToManyField(User, related_name='belonging_groups')
    title = models.CharField(max_length=2048)

    def __unicode__(self):
        return self.title

class Payment(models.Model):
    group_payment = models.ForeignKey(GroupPayment)
    user = models.ForeignKey(User, related_name='payments')
    value = models.FloatField()
    paid = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s for %s' % (self.group_payment, self.user)

    def send_email(self):
        from django.core.mail import send_mail
        from django.template.loader import render_to_string
        subject = "New payment: %s - %f" % (self.group_payment.title, self.value)
        body = render_to_string('email/payment.txt', {'payment': self})
        send_email(subject, body, 'from@example.com', [self.user.email])

class UserPaymentManager(models.Manager):

    def set_value(self, from_user, to_user, value):
        user_payment, _ = self.get_or_create(from_user=from_user, to_user=to_user)
        user_payment.value = value
        user_payment.save()

    def update_for(self, from_user, to_user):
        qs1 = Payment.objects.filter(user=from_user, paid=False, group_payment__user=to_user)
        value1 = qs1.aggregate(Sum('value'))['value__sum'] or 0

        qs2 = Payment.objects.filter(user=to_user, paid=False, group_payment__user=from_user)
        value2 = qs2.aggregate(Sum('value'))['value__sum'] or 0

        self.set_value(from_user, to_user, value1-value2)
        self.set_value(to_user, from_user, value2-value1)

class UserPayment(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user_payments')
    to_user = models.ForeignKey(User, related_name='to_user_payments')
    value = models.FloatField(default=0)

    objects = UserPaymentManager()

    class Meta:
        unique_together = ('from_user', 'to_user')


class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends')
    friend = models.ForeignKey(User)

@receiver(post_save, sender=Payment)
def payment_post_save(sender, instance, **kwargs):
    UserPayment.objects.update_for(instance.user, instance.group_payment.user)

