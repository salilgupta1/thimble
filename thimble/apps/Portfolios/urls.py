from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import create, community, render

urlpatterns = patterns('',
    # render
    url(r'^$', render.render_portfolio, name='render_portfolio'),
    url(r'^story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/$', render.render_design_story, name='render_design_story'),

    # create
    url(r'^create_design_story/$', create.create_design_story, name='create_design_story'),
    url(r'^story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/create_chapter/$', create.create_chapter, name='create_chapter'),

    # edit
    url(r'^story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/edit_chapter/(?P<entry_id>[0-9]+)/$', create.edit_chapter, name='edit_chapter'),
    url(r'^edit_story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/$', create.edit_story, name='edit_story'),

    # community activites
    # like
    url(r'^like_story/$', community.like_design_story, name='like_design_story'),
    url(r'^unlike_story/$', community.unlike_design_story, name='unlike_design_story'),

    # follow
    url(r'^follow/$', community.follow_designer, name='follow_designer'),
    url(r'^unfollow/$', community.unfollow_designer, name='unfollow_designer'),

    # comment
    url(r'^comment/$', community.comment, name='comment'),

)
