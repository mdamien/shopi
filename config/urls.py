from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

SLUG_REGEX = r'[-a-zA-Z0-9_]+'

urlpatterns = patterns('',
    url(r'^$', 'shops.views.home', name='home'),
    url(r'^(?P<slug>%s)/$' % SLUG_REGEX, 'shops.views.detail', name='shop'),

    url(r'^admin/', include(admin.site.urls)),
)
