from django.conf.urls import patterns, include, url
from thimble.apps.Portfolios.views import create, community, render

urlpatterns = patterns('',
    # render
    url(r'^$', render.render_portfolio, name='render_portfolio'),
    url(r'^collection/(?P<collection_id>[0-9]+)-(?P<slug>[\w-]+)/$', render.render_collection, name='render_collection'),

    # create
    url(r'^create-collection/$', create.create_collection, name='create_collection'),

    url(r'^edit-collection/(?P<collection_id>[0-9]+)-(?P<slug>[\w-]+)/$', create.edit_collection, name='edit_collection'),

    # community activites
    # like/unlike
    url(r'^liking/$', community.liking, name='liking'),

    # following
    url(r'^following/$', community.following, name='following'),

    # comment
    url(r'^comment/$', community.comment, name='comment'),
)
