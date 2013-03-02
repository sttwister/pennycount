
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
    class Meta:
        queryset = Payment.objects.all()
        resource_name = 'payment'
        list_allowed_methods = ['get', 'post']
        authorization = Authorization()
        authentication = SessionAuthentication()

