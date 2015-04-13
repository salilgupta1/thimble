from django.conf.urls import patterns, include, url
from thimble.apps.landingpage.views import views
urlpatterns = patterns('',
    url(r'new-home-page/$', views.home, name='home'),
    url(r'^$', views.landingpage, name='old_landingpage')
)
