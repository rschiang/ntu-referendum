from django.conf.urls import patterns, include, url

urlpatterns = patterns('auth.views',
    url(r'^$', 'home'),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
)
