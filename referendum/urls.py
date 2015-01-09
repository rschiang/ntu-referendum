from django.conf.urls import patterns, include, url

urlpatterns = patterns('referendum.views',
    url(r'^$', 'home'),
    url(r'^done/$', 'done'),
    url(r'^(?P<refid>\d+)/$', 'ballot'),
    url(r'^(?P<refid>\d+)/cast/$', 'vote'),
)
