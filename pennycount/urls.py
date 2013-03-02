from django.conf.urls import patterns, include, url
from django.contrib import admin

from .api import v1_api

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pennycount.views.index'),
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
