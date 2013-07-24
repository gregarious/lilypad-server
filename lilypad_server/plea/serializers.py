from rest_framework import serializers
from common.serializers import NamespacedHyperlinkedModelSerializer, stub_serializer_factory

from plea.models import Student, BehaviorIncidentType, BehaviorIncident
from plea.models import Topic, Subtopic, InputChannel, OutputChannel
from plea.models import Chart, DayMetric, PhaseLine

class StudentSerializer(NamespacedHyperlinkedModelSerializer):
    behavior_types_url = serializers.HyperlinkedIdentityField(
        view_name='plea:student_behaviortype-list')
    behavior_incidents_url = serializers.HyperlinkedIdentityField(
        view_name='plea:student_behaviorincident-list')

    charts_url = serializers.HyperlinkedIdentityField(
        view_name='plea:student_chart-list')

    class Meta:
        model = Student
        fields = ('url', 'id', 'first_name', 'last_name', 'date_of_birth',
            'behavior_types_url', 'behavior_incidents_url')

class BehaviorIncidentTypeSerializer(NamespacedHyperlinkedModelSerializer):
    applicable_student = stub_serializer_factory(Student)

    class Meta:
        model = BehaviorIncidentType
        fields = ('id', 'url', 'label', 'code', 'active', 'student')

class BehaviorIncidentSerializer(NamespacedHyperlinkedModelSerializer):
    student = stub_serializer_factory(Student)
    type = BehaviorIncidentTypeSerializer()

    class Meta:
        model = BehaviorIncident
        fields = ('id', 'url', 'type', 'occurred_at' 'comment', 'student')

class SubtopicSerializer(NamespacedHyperlinkedModelSerializer):
    class Meta:
        model = Subtopic
        fields = ('id', 'url', 'name', 'menu_order')

class TopicSerializer(NamespacedHyperlinkedModelSerializer):
    subtopics = SubtopicSerializer()

    class Meta:
        model = Topic
        fields = ('id', 'url', 'name', 'menu_order', 'subtopics')

class InputChannelSerializer(NamespacedHyperlinkedModelSerializer):
    class Meta:
        model = InputChannel
        fields = ('id', 'url', 'name', 'menu_order')

class OutputChannelSerializer(NamespacedHyperlinkedModelSerializer):
    class Meta:
        model = OutputChannel
        fields = ('id', 'url', 'name', 'menu_order')

class ChartSerializer(NamespacedHyperlinkedModelSerializer):
    topic = stub_serializer_factory(Topic)
    subtopic = stub_serializer_factory(Subtopic)
    input_channel = stub_serializer_factory(InputChannel)
    output_channel = stub_serializer_factory(OutputChannel)
    student = stub_serializer_factory(Student)

    day_metrics_url = serializers.HyperlinkedIdentityField(
        view_name='pace:chart_daymetric-list')

    class Meta:
        model = Chart
        fields = ('id', 'url', 'created_at', 'last_opened_at', 'topic', 'subtopic', 'input_channel', 'output_channel', 'label', 'student')

class DayMetricSerializer(NamespacedHyperlinkedModelSerializer):
    chart = stub_serializer_factory(Chart)

    class Meta:
        model = DayMetric
        fields = ('id', 'url', 'date', 'value', 'type', 'chart',)

class PhaseLineSerializer(NamespacedHyperlinkedModelSerializer):
    chart = stub_serializer_factory(Chart)

    class Meta:
        model = PhaseLine
        fields = ('id', 'title', 'date', 'chart',)
