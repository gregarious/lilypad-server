from rest_framework import serializers
from rest_framework.reverse import reverse
from pace.models import Student, PeriodicRecord, BehaviorIncidentType, BehaviorIncident

from django.core.urlresolvers import NoReverseMatch
from copy import copy

class StudentStubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'url')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: make these links to special student subresource views
    periodic_records_url = serializers.HyperlinkedIdentityField(
        view_name='student_periodicrecord-list')
    behavior_types_url = serializers.HyperlinkedIdentityField(
        view_name='student_behaviortype-list')
    behavior_incidents_url = serializers.HyperlinkedIdentityField(
        view_name='student_behaviorincident-list')

    class Meta:
        model = Student
        fields = ('url', 'id', 'first_name', 'last_name',
            'periodic_records_url', 'behavior_types_url',
            'behavior_incidents_url')

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
    student = StudentStubSerializer()
    class Meta:
        model = PeriodicRecord
        fields = ('id', 'url', 'last_changed_at', 'period', 'date',
            'student', 'is_eligible', 'kind_words_points',
            'complete_work_points', 'follow_directions_points',
            'be_safe_points')

class BehaviorIncidentTypeSerializer(serializers.HyperlinkedModelSerializer):
    applicable_student = StudentStubSerializer()
    class Meta:
        model = BehaviorIncidentType
        fields = ('id', 'url', 'label', 'code', 'supports_duration',
            'applicable_student')

class BehaviorIncidentSerializer(serializers.HyperlinkedModelSerializer):
    student = StudentStubSerializer()
    type = BehaviorIncidentTypeSerializer()
    class Meta:
        model = BehaviorIncident
        fields = ('id', 'url', 'type', 'started_at', 'ended_at', 'comment',
            'student', 'last_modified_at')
