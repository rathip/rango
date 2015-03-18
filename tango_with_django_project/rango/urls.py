from django.conf.urls import patterns, url
from rango import views

##urlpatterns = patterns('',
##        url(r'^$', views.index, name='index'),
##        url(r'^about/$', views.about, name='about'),
##        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
##    url(r'^add_page/$', views.add_page, name='add_page'), # NEW MAPPING!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'), # NEW MAPPING!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category1, name='category1'))  # New!