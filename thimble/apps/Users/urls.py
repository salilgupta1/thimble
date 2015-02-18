from django.conf.urls import patterns, include, url
from thimble.apps.Users.views import views

urlpatterns = patterns('',
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^create_account/$', views.create_account, name='create_account'),
)