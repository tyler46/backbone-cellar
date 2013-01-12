from django.conf.urls.defaults import *
from tastypie.api import Api

from wines.api.resources import WineResource

v1_api = Api(api_name='v1')
v1_api.register(WineResource())

wine_resource = WineResource()

urlpatterns = patterns('wines.api.urls',
    # The normal jazz here...
    (r'^', include(v1_api.urls)),
)
