from django.db.models import Q

from plea.models import Student, BehaviorIncidentType, BehaviorIncident
from plea.models import Topic, Subtopic, InputChannel, OutputChannel
from plea.models import Chart, DayMetric, PhaseLine

from plea.serializers import StudentSerializer
from plea.serializers import BehaviorIncidentSerializer, BehaviorIncidentTypeSerializer
from plea.serializers import TopicSerializer, SubtopicSerializer, InputChannelSerializer, OutputChannelSerializer
from plea.serializers import ChartSerializer, DayMetricSerializer, PhaseLineSerializer, OutputChannelSerializer

from django.http import Http404
from rest_framework import generics

from django.contrib.staticfiles.views import serve

def index(request):
    return serve(request, 'lilypad-plea/index.html')

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BehaviorIncidentTypeList(generics.ListAPIView):
    queryset = BehaviorIncidentType.objects.all()
    serializer_class = BehaviorIncidentTypeSerializer

class BehaviorIncidentTypeDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncidentType.objects.all()
    serializer_class = BehaviorIncidentTypeSerializer

class StudentBehaviorIncidentTypeList(generics.ListAPIView):
    serializer_class = BehaviorIncidentTypeSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        records = BehaviorIncidentType.objects.filter(student__pk=pk)
        return records

class BehaviorIncidentList(generics.ListAPIView):
    queryset = BehaviorIncident.objects.all()
    serializer_class = BehaviorIncidentSerializer

class BehaviorIncidentDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncident.objects.all()
    serializer_class = BehaviorIncidentSerializer

class StudentBehaviorIncidentList(generics.ListAPIView):
    serializer_class = BehaviorIncidentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        records = BehaviorIncident.objects.filter(student__pk=pk)
        return records


class TopicList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class TopicDetail(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class SubtopicDetail(generics.RetrieveAPIView):
    queryset = Subtopic.objects.all()
    serializer_class = SubtopicSerializer

class InputChannelList(generics.ListAPIView):
    queryset = InputChannel.objects.all()
    serializer_class = InputChannelSerializer

class InputChannelDetail(generics.RetrieveAPIView):
    queryset = InputChannel.objects.all()
    serializer_class = InputChannelSerializer

class OutputChannelList(generics.ListAPIView):
    queryset = OutputChannel.objects.all()
    serializer_class = OutputChannelSerializer

class OutputChannelDetail(generics.RetrieveAPIView):
    queryset = OutputChannel.objects.all()
    serializer_class = OutputChannelSerializer



class ChartList(generics.ListAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

class ChartDetail(generics.RetrieveAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

class StudentChartList(generics.ListAPIView):
    serializer_class = ChartSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        charts = Chart.objects.filter(student__pk=pk)
        return charts

class DayMetricList(generics.ListAPIView):
    queryset = DayMetric.objects.all()
    serializer_class = DayMetricSerializer

class DayMetricDetail(generics.RetrieveAPIView):
    queryset = DayMetric.objects.all()
    serializer_class = DayMetricSerializer

class ChartDayMetricList(generics.ListAPIView):
    serializer_class = DayMetricSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        charts = DayMetric.objects.filter(chart__pk=pk)
        return charts

class PhaseLineList(generics.ListAPIView):
    queryset = PhaseLine.objects.all()
    serializer_class = PhaseLineSerializer

class PhaseLineDetail(generics.RetrieveAPIView):
    queryset = PhaseLine.objects.all()
    serializer_class = PhaseLineSerializer

class ChartPhaseLineList(generics.ListAPIView):
    serializer_class = PhaseLineSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        charts = PhaseLine.objects.filter(chart__pk=pk)
        return charts
