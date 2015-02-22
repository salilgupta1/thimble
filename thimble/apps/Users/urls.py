from django.conf.urls import patterns, include, url
from thimble.apps.Users.views import views

urlpatterns = patterns('',
	url(r'^create_account/$', views.create_account, name='create_account'),
	url(r'^create_account/complete$', views.direct_upload_complete, name='direct_upload_complete'),
)