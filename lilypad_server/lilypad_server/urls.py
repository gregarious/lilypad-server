from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pace import urls as pace_urls

urlpatterns = patterns('',
    url(r'^$', 'lilypad_server.views.home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^pace/', include(pace_urls))
)
