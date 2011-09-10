from tastypie.resources import ModelResource

from common.models import Something

class SomethingResource(ModelResource):
    class Meta:
        queryset = Something.objects.all()
        resource_name = "something"
