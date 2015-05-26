from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import create, community, render

urlpatterns = patterns('',
    # render
    url(r'^$', render.render_portfolio, name='render_portfolio'),
    url(r'^collection/(?P<collection_id>[0-9]+)-(?P<slug>[\w-]+)/$', render.render_collection, name='render_collection'),

    # create
    #url(r'^create-collection/$', create.create_collection, name='create_collection'),
    #url(r'^story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/create-chapter/$', create.create_chapter, name='create_chapter'),

    # edit
    #url(r'^story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/edit-chapter/(?P<entry_id>[0-9]+)/$', create.edit_chapter, name='edit_chapter'),
    #url(r'^edit-story/(?P<story_id>[0-9]+)-(?P<slug>[\w-]+)/$', create.edit_story, name='edit_story'),

    # community activites
    # like/unlike
    url(r'^liking/$', community.liking, name='liking'),

    # following
    url(r'^following/$', community.following, name='following'),

    # comment
    url(r'^comment/$', community.comment, name='comment'),
)
