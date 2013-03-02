from django.contrib.auth.models import User

from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from .models import Payment

class UserResourceMixin(object):
    def obj_create(self, bundle, request=None, **kwargs):
        return super(EnvironmentResource, self).obj_create(bundle, request, user=request.user)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)


class PaymentResource(ModelResource, UserResourceMixin):
    shared_with = fields.ToManyField('pennycount.api.UserResource', 'shared_with', full=True)

    class Meta:
        queryset = Payment.objects.all()
        resource_name = 'payment'
        list_allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = SessionAuthentication()

class UserResource(ModelResource, UserResourceMixin):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'email']
        list_allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = SessionAuthentication()
