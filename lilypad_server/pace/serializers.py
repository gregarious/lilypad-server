from rest_framework import serializers
from rest_framework.reverse import reverse
from pace.models import Student, PeriodicRecord, BehaviorIncidentType, BehaviorIncident

from django.core.urlresolvers import NoReverseMatch
from copy import copy

# needed for old URL scheme -- not necessary anymore?
# class ExtraArgsHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
#     def __init__(self, *args, **kwargs):
#         self.extra_kwargs = kwargs.pop('extra_kwargs', {})
#         super(ExtraArgsHyperlinkedIdentityField, self).__init__(*args, **kwargs)

#     def get_url(self, obj, view_name, request, format):
#         '''
#         Mimics base class's `get_url` field, inserting the extra kwargs
#         into the reverse call, and trimming out all the special cases
#         we're not intending to use.
#         '''
#         lookup_field = getattr(obj, self.lookup_field)
#         kwargs = copy(self.extra_kwargs)
#         kwargs.update({self.lookup_field: lookup_field})
#         return reverse(view_name, kwargs=kwargs, request=request, format=format)

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    periodic_records = serializers.HyperlinkedRelatedField(many=True,
        read_only=True, view_name='periodicrecord-detail')
    behavior_incidents = serializers.HyperlinkedRelatedField(many=True,
        read_only=True, view_name='behaviorincident-detail')

    class Meta:
        model = Student
        fields = ('url', 'id', 'first_name', 'last_name',
            'periodic_records', 'behavior_incidents')

# Might be useful for serializing point records into a dict
#
# class PointRecords(object):
#     def __init__(self, kw, cd, fd, bs):
#         self.kw = kw
#         self.cd = cd
#         self.fd = fd
#         self.bs = bs

# class PointRecordsField(serializers.WritableField):
#     def field_from_native(self, data, files, field_name, into):
#         return PointRecords(
#             kw=data.get('kw', None),
#             cd=data.get('cd', None),
#             fd=data.get('fd', None),
#             bs=data.get('bs', None)
#         )

#     def field_to_native(self, obj, field_name):
#         return {
#             'kw': obj.kind_words_points,
#             'cw': obj.complete_work_points,
#             'fd': obj.follow_directions_points,
#             'bs': obj.be_safe_points
#         }

class PeriodicRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PeriodicRecord
        fields = ('id', 'url', 'last_changed_at', 'period', 'date',
            'student', 'is_eligible', 'kind_words_points',
            'complete_work_points', 'follow_directions_points',
            'be_safe_points')

class BehaviorIncidentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BehaviorIncidentType
        fields = ('id', 'url', 'label', 'code', 'supports_duration',
            'applicable_student')

class BehaviorIncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BehaviorIncident
        fields = ('id', 'url', 'type', 'started_at', 'ended_at', 'comment',
            'student', 'last_modified_at')
