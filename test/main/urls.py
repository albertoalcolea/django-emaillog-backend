from django.conf.urls import patterns, include, url

from main import views

urlpatterns = patterns('',
	# Common
	url(r'^$', views.index, name='index'),
)