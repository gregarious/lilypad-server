from rest_framework import serializers
from common.serializers import NamespacedHyperlinkedModelSerializer, stub_serializer_factory

from django.contrib.auth.models import User
from pace.models import Student, PeriodicRecord, PointLoss,     \
                        BehaviorIncidentType, BehaviorIncident, \
                        Post, ReplyPost, AttendanceSpan

class StudentSerializer(NamespacedHyperlinkedModelSerializer):
    periodic_records_url = serializers.HyperlinkedIdentityField(
        view_name='pace:student_periodicrecord-list')
    point_losses_url = serializers.HyperlinkedIdentityField(
        view_name='pace:student_pointloss-list')
    behavior_types_url = serializers.HyperlinkedIdentityField(
        view_name='pace:student_behaviortype-list')
    behavior_incidents_url = serializers.HyperlinkedIdentityField(
        view_name='pace:student_behaviorincident-list')
    posts_url = serializers.HyperlinkedIdentityField(
        view_name='pace:student_post-list')
    attendancespans_url = serializers.HyperlinkedIdentityField(
        view_name='pace:student_attendancespan-list')

    class Meta:
        model = Student
        fields = ('url', 'id', 'first_name', 'last_name',
            'periodic_records_url', 'point_losses_url',
            'behavior_types_url', 'behavior_incidents_url',
            'posts_url', 'attendancespans_url')

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

class PeriodicRecordSerializer(NamespacedHyperlinkedModelSerializer):
    student = stub_serializer_factory(Student)

    class Meta:
        model = PeriodicRecord
        fields = ('id', 'url', 'last_changed_at', 'period', 'date',
            'student', 'is_eligible', 'kind_words_points',
            'complete_work_points', 'follow_directions_points',
            'be_safe_points')

class PointLossSerializer(NamespacedHyperlinkedModelSerializer):
    periodic_record = stub_serializer_factory(PeriodicRecord)

    class Meta:
        model = PointLoss
        fields = ('id', 'url', 'occurred_at', 'periodic_record',
            'point_type', 'comment')

class BehaviorIncidentTypeSerializer(NamespacedHyperlinkedModelSerializer):
    applicable_student = stub_serializer_factory(Student)

    class Meta:
        model = BehaviorIncidentType
        fields = ('id', 'url', 'label', 'code', 'supports_duration',
            'applicable_student')

class BehaviorIncidentSerializer(NamespacedHyperlinkedModelSerializer):
    student = stub_serializer_factory(Student)
    type = BehaviorIncidentTypeSerializer()

    class Meta:
        model = BehaviorIncident
        fields = ('id', 'url', 'type', 'started_at', 'ended_at', 'comment',
            'student', 'last_modified_at')

class ReplyPostSerializer(serializers.ModelSerializer):
    # TODO: make this a true User stub when user model worked out
    author = serializers.RelatedField()

    class Meta:
        model = ReplyPost
        fields = ('author', 'content', 'created_at')

class PostSerializer(NamespacedHyperlinkedModelSerializer):
    # TODO: make this a true User stub when user model worked out
    author = serializers.RelatedField()
    student = stub_serializer_factory(Student)
    replies = ReplyPostSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'url', 'author', 'student', 'content', 'created_at', 'replies')

class AttendanceSpanSerializer(NamespacedHyperlinkedModelSerializer):
    student = stub_serializer_factory(Student)

    class Meta:
        model = AttendanceSpan
        fields = ('id', 'url', 'student', 'date', 'time_in', 'time_out')
