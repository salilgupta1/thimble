from django.conf.urls import patterns, include, url
from thimble.apps.landingpage.views import views
urlpatterns = patterns('',
    url(r'home/$', views.home, name='home'),
    url(r'^$', views.landingpage, name='new_landingpage'),
    url(r'about/$', views.oldlandingpage, name='old_landingpage')
)
