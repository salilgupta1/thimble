from django.conf.urls import patterns, include, url
from thimble.apps.contests.views import views
urlpatterns = patterns('',
	url(r'^$', views.contests, name='contests_page'),
	url(r'^shirts/$', views.shirts, name='shirts_contest'),
	url(r'^results/$', views.results, name='results_page'),
	url(r'^shop/$', views.shop, name='shop_page'),
)