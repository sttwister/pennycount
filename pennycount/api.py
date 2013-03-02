from django.contrib.auth.models import User

from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

from .models import GroupPayment, Payment, Friend

class UserResourceMixin(object):
    def obj_create(self, bundle, request=None, **kwargs):
        return super(EnvironmentResource, self).obj_create(bundle, request, user=request.user)

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)


class GroupPaymentResource(UserResourceMixin, ModelResource):
    shared_with = fields.ToManyField('pennycount.api.UserResource', 'shared_with', full=True)

    class Meta:
        queryset = GroupPayment.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()

class PaymentResource(UserResourceMixin, ModelResource):
    group_payment = fields.ToManyField('pennycount.api.GroupPaymentResource', 'shared_with', full=True)
    user = fields.ToManyField('pennycount.api.UserResource', 'shared_with', full=True)

    class Meta:
        queryset = Payment.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()


class UserResource(UserResourceMixin, ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['username', 'first_name', 'last_name', 'email']
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()

class FriendResource(UserResourceMixin, ModelResource):
    friend = fields.ForeignKey('pennycount.api.UserResource', 'friend', full=True)

    class Meta:
        queryset = Friend.objects.all()
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()

v1_api = Api(api_name='v1')
v1_api.register(GroupPaymentResource())
v1_api.register(PaymentResource())
v1_api.register(UserResource())
v1_api.register(FriendResource())
