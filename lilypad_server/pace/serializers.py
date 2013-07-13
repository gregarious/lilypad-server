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

    # behavior_point_record_collection = serializers.HyperlinkedIdentityField(
    #     view_name='globalbehaviorpointrecord-list')

    # no tests written yet
    # discussion_collection = serializers.HyperlinkedIdentityField(
    #     view_name='discussion-list')

    periodic_records = serializers.HyperlinkedRelatedField(many=True,
        read_only=True, view_name='periodicrecord-detail')
    behavior_incidents = serializers.HyperlinkedRelatedField(many=True,
        read_only=True, view_name='behaviorincident-detail')

    class Meta:
        model = Student
        fields = ('url', 'id', 'first_name', 'last_name',
            'periodic_records', 'behavior_incidents')


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

#     def __init__(self, *args, **kwargs):
#         try:
#             student_pk = kwargs.pop('student_pk')
#         except KeyError:
#             raise ValueError('GlobalBehaviorPointRecordSerializer must be'
#                 'initialized with the parent `student_pk`')

#         super(GlobalBehaviorPointRecordSerializer, self).__init__(*args, **kwargs)
#         self.fields['url'] = ExtraArgsHyperlinkedIdentityField(
#             view_name='globalbehaviorpointrecord-detail',
#             extra_kwargs={'student_pk': student_pk})
