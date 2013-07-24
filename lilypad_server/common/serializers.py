from rest_framework import serializers

class NamespacedHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Same as HyperlinkedModelSerializer, but includes app namespace in the
    url resolving.
    '''
    _default_view_name = '%(app_label)s:%(model_name)s-detail'
