from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import views


urlpatterns = patterns('',
	url(r'^$', views.render_portfolio, name='render_portfolio'),
	url(r'^edit/$', views.edit_portfolio, name='edit_portfolio'),
	url(r'^story/(?P<story_id>[0-9]+)/$', views.render_design_story, name='render_design_story'),
)