from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # landing page
    url(r'^', include('thimble.apps.landingpage.urls', namespace='landingpage')),

    # Users app
    url(r'^users/',include('thimble.apps.Users.urls', namespace="Users")),

    # Portfolios app
    url(r'^portfolios/',include('thimble.apps.Portfolios.urls', namespace="Portfolios"))
)
