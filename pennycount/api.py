import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q

from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, Resource

from .models import GroupPayment, Payment, UserPayment, Friend

class UserResourceMixin(object):

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)


class GroupPaymentResource(UserResourceMixin, ModelResource):
    shared_with = fields.ToManyField('pennycount.api.UserResource', 'shared_with', full=True, null=True)
    user = fields.ForeignKey('pennycount.api.UserResource', 'user', full=True)

    class Meta:
        queryset = GroupPayment.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        for email in bundle.data.get('emails', []):
            validate_email(email)

        result = super(GroupPaymentResource, self).obj_create(bundle, user=bundle.request.user, **kwargs)

        for email in bundle.data.get('emails', []):
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User.objects.create(email=email, username=str(uuid.uuid4()))
                Friend.objects.create(user=user, friend=bundle.request.user)
                Friend.objects.create(user=bundle.request.user, friend=user)

            bundle.obj.shared_with.add(user)

        bundle.obj.create_payments()

        return result

class PaymentResource(UserResourceMixin, ModelResource):
    group_payment = fields.ForeignKey('pennycount.api.GroupPaymentResource', 'group_payment', full=True)
    user = fields.ForeignKey('pennycount.api.UserResource', 'user', full=True)

    class Meta:
        queryset = Payment.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        always_return_data = True


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['username', 'first_name', 'last_name', 'email']
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        always_return_data = True

class FriendResource(UserResourceMixin, ModelResource):
    friend = fields.ForeignKey('pennycount.api.UserResource', 'friend', full=True)

    class Meta:
        queryset = Friend.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        always_return_data = True

class UserPaymentResource(ModelResource):
    from_user = fields.ForeignKey('pennycount.api.UserResource', 'from_user', full=True)
    to_user = fields.ForeignKey('pennycount.api.UserResource', 'to_user', full=True)

    class Meta:
        queryset = UserPayment.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()
        always_return_data = True

    def authorized_read_list(self, object_list, bundle):
        user = bundle.request.user
        return object_list.filter(to_user=user)

v1_api = Api(api_name='v1')
v1_api.register(GroupPaymentResource())
v1_api.register(PaymentResource())
v1_api.register(UserResource())
v1_api.register(FriendResource())
v1_api.register(UserPaymentResource())
