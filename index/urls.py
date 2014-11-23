from django.conf.urls import patterns, url
from index import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/',views.about, name='about'),
					   url(r'^printers/',views.printers, name='printers'))
