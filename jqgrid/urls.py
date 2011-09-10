from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from common.api import SomethingResource

something_resource = SomethingResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jqgrid.views.home', name='home'),
    # url(r'^jqgrid/', include('jqgrid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(something_resource.urls)),
)

urlpatterns += staticfiles_urlpatterns()
