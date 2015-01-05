from django.conf.urls import patterns, include, url

urlpatterns = patterns('referendum.views',
    url(r'^$', 'home'),
    url(r'^done/$', 'done'),
    url(r'^cast/$', 'vote'),
    url(r'^(?P<refid>\d+)/$', 'ballot'),
)
