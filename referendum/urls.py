from django.conf.urls import patterns, include, url

urlpatterns = patterns('referendum.views',
    url(r'^$', 'home'),
    url(r'^done/$', 'done'),
    url(r'^next/$', 'next_ballot'),
    url(r'^(?P<ref_id>\d+)/$', 'ballot'),
    url(r'^(?P<ref_id>\d+)/cast/$', 'vote'),
)
