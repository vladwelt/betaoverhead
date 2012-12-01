from django.conf.urls import patterns, include, url
from users.views import user_profile, profile
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'betaoverhead.views.home', name='home'),
    # url(r'^betaoverhead/', include('betaoverhead.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url('^$','django.views.generic.simple.direct_to_template',{'template':'home.html'}),
    url(r'^accounts/', include('registration.urls')),
    url(r'^profile/user/(?P<id>\d+)$',user_profile,name='user_profile'),
    url(r'^profile/$', profile),
)
