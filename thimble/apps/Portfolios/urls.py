from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import views


urlpatterns = patterns('',
	url(r'^(?P<subdomain>[-a-zA-Z0-9_]+)/$',views.render_portfolio, name='render_portfolio'),
	url(r'^edit/(?P<subdomain>[-a-zA-Z0-9_]+)/$',views.edit_portfolio, name='edit_portfolio'),
	url(r'^upload/(?P<subdomain>[-a-zA-Z0-9_]+)/$', views.image_upload, name='image_upload'),
	url(r'^upload_prompt/(?P<subdomain>[-a-zA-Z0-9_]+)/$', views.upload_prompt, name='upload_prompt'),
	url(r'^direct_upload_complete/(?P<subdomain>[-a-zA-Z0-9_]+)/$', views.direct_upload_complete, name='direct_upload_complete'),
)