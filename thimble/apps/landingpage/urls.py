from django.conf.urls import patterns, include, url
from thimble.apps.landingpage.views import views
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'old-landingpage/$', views.landingpage, name='old_landingpage')
)
