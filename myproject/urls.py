from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^messages/', include('privatemessages.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
