from django.conf.urls import patterns, include, url
from thimble.apps.landingpage.views import views
urlpatterns = patterns('',
    url(r'home/$', views.home, name='home'),
    url(r'dashboard/(?P<username>[-a-zA-Z0-9_]+)$', views.dashboard, name='dashboard'),
    url(r'filter-collections/$', views.filter_by_tags, name='filter_by_tags'),
    url(r'list-followers/$', views.render_followers_list, name='render_followers_list'),
    url(r'list-favorites/$', views.render_favorites_list, name='render_favorites_list'),
    url(r'^$', views.landingpage, name='new_landingpage'),
    url(r'about/$', views.oldlandingpage, name='old_landingpage')
)
