from django.conf.urls import patterns, include, url
from thimble.apps.landingpage.views import views

urlpatterns = patterns('',
        url(r'^$', views.landingpage, name='landingpage'),
)
