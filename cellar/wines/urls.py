from django.conf.urls.defaults import *

urlpatterns = patterns('wines.views',
    url(r'^$', 'index'),
    url(r'^(\d+)/$', 'detail', name='wine_detail'),
)
