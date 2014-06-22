from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TripPlan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # default page
    url(r'^$', 'TripPlan.dashboard.views.index'),

    # customized yelp search url
    url(r'^search/', 'TripPlan.dashboard.views.user_input'),
)
