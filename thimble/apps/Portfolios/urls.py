from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import views

urlpatterns = patterns('',
	# render
	url(r'^$', views.render_portfolio, name='render_portfolio'),
	url(r'^story/(?P<story_id>[0-9]+)/$', views.render_design_story, name='render_design_story'),

	# create 
	url(r'^create_design_story/$', views.create_design_story, name='create_design_story'),
	url(r'^create_chapter/$', views.create_chapter, name='create_chapter'),

	# community activites
	# like
	url(r'^like_story/$', views.like_design_story, name='like_design_story'),
	url(r'^unlike_story/$', views.unlike_design_story, name='unlike_design_story'),

	# follow
	url(r'^follow/$', views.follow_designer, name='follow_designer'),
	url(r'^unfollow/$', views.unfollow_designer, name='unfollow_designer'),

	
)
