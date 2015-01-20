from django.conf.urls import patterns, include, url
from ednu.apps.landingpage.views import views

urlpatterns = patterns('',
        url(r'^$', views.landingpage, name='landingpage'),
)