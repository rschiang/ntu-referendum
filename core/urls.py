from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    url(r'^account/', include('auth.urls')),
    url(r'^referendum/', include('referendum.urls')),
)
