from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import views

urlpatterns = patterns('',
	url(r'^$', views.render_portfolio, name='render_portfolio'),
	
	#url(r'^create_design_story/$', views.create_design_story, name='create_design_story'),
	#url(r'^story/(?P<story_id>[0-9]+)-story-name/$', views.render_design_story, name='render_design_story'),
)