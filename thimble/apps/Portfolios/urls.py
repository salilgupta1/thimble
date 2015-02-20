from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import views


urlpatterns = patterns('',
	url(r'^(?P<subdomain>[-a-zA-Z0-9_]+)/$',views.render_portfolio, name='render_portfolio'),
	url(r'^edit/(?P<subdomain>[-a-zA-Z0-9_]+)/$',views.edit_portfolio, name='edit_portfolio'),
)