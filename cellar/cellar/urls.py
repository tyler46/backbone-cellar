from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.views.static import *

import wines

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/admin/'}),
    url(r'^wines/', include('wines.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('wines.api.urls')),
)

if settings.LOCAL_DEVELOPMENT:
    urlpatterns += patterns('django.views',
            url(r'%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                'static.serve', {'document_root': settings.MEDIA_ROOT,}),
    )
