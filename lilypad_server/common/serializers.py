from rest_framework import serializers

class NamespacedHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Same as HyperlinkedModelSerializer, but includes app namespace in the
    url resolving.
    '''
    _default_view_name = '%(app_label)s:%(model_name)s-detail'

def stub_serializer_factory(model_class):
    '''
    Returns a NamespacedHyperlinkedModelSerializer for the given model
    class that exposes the resource's `id` and `url` only.
    '''
    meta_class = type('Meta', (), {
        'model': model_class,
        'fields': ('id', 'url',)
    })

    stub_class = type("%sStubSerialier" % model_class.__name__,
        (NamespacedHyperlinkedModelSerializer,),
        {'Meta': meta_class}
    )

    return stub_class()
