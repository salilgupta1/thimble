from django.conf.urls import patterns, include, url
from django.contrib import admin
from thimble.apps.Manage_Cloudinary.views import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/cloudinary', views.render_cloudinary, name='render_cloudinary'),
    url(r'^admin/', include(admin.site.urls)),
    
    # landing page
    url(r'^', include('thimble.apps.landingpage.urls', namespace='landingpage')),

    # Users app
    url(r'^accounts/',include('thimble.apps.Users.urls', namespace="Users")),

    # Portfolios app
   	url(r'^(?P<username>[-a-zA-Z0-9_]+)/',include('thimble.apps.Portfolios.urls', namespace="Portfolios"))
)

handler404 = 'thimble.views.handler404'
handler500 = 'thimble.views.handler500'