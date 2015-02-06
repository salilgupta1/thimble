from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thimble.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # landing page
    url(r'^', include('thimble.apps.landingpage.urls', namespace='landingpage')),
    # contests
    url(r'^mvp/', include('thimble.apps.contests.urls', namespace='contests')),
)
