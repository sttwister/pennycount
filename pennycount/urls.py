from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from .api import PaymentResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PaymentResource())


urlpatterns = patterns('',
    url(r'^$', 'pennycount.views.index'),
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
