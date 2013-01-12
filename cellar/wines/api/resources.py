import copy

from tastypie.resources import ModelResource
from wines.models import Wine

class WineResource(ModelResource):
    """Wine Resource."""
    class Meta:
        queryset = Wine.objects.all()
        resource_name = 'wine'

    def alter_list_data_to_serialize(self, request, data_dict):
        """ Return instead of name objects the corresponding model's resource name. """
        if isinstance(data_dict, dict):
            data_dict['wines'] = copy.copy(data_dict['objects'])
            del(data_dict['objects'])
        return data_dict
            
