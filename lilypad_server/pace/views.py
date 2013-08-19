from django.db.models import Q

from pace.models import Student, PeriodicRecord, PointLoss,     \
                        BehaviorIncidentType, BehaviorIncident, \
                        Post, ReplyPost, AttendanceSpan

from pace.serializers import StudentSerializer, PeriodicRecordSerializer,     \
                             PointLossSerializer, BehaviorIncidentSerializer, \
                             BehaviorIncidentTypeSerializer, PostSerializer,  \
                             AttendanceSpanSerializer

from django.http import Http404, HttpResponse
from rest_framework import generics

from django.contrib.staticfiles.views import serve

from dateutil import parser

def index(request):
    try:
        return serve(request, 'lilypad-pace/index.html')
    except Http404:
        return HttpResponse('Server is configured incorrectly: '
            'no index.html file was found for the Pace app.', status=404)

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class PeriodicRecordList(generics.ListAPIView):
    serializer_class = PeriodicRecordSerializer
    def get_queryset(self):
        queryset = PeriodicRecord.objects.all()
        for key in ('date', 'date__gte', 'date__gt', 'date_gte', 'date__lt',):
            iso_string = self.request.QUERY_PARAMS.get(key, None)
            if iso_string:
                queryset = queryset.filter(**{key: parser.parse(iso_string).date()})
        return queryset

class PeriodicRecordDetail(generics.RetrieveAPIView):
    queryset = PeriodicRecord.objects.all()
    serializer_class = PeriodicRecordSerializer

class StudentPeriodicRecordList(PeriodicRecordList):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        queryset = super(StudentPeriodicRecordList, self).get_queryset()
        return queryset.filter(student__pk=pk)

class PointLossList(generics.ListAPIView):
    serializer_class = PointLossSerializer

    # TODO: enable POST/PUT functionality that calls PeriodicRecord.declare_point_loss

    def get_queryset(self):
        queryset = PointLoss.objects.all()
        for key in ('occurred_at', 'occurred_at__gt', 'occurred_at__gte', 'occurred_at__lt', 'occurred_at__lte'):
            iso_string = self.request.QUERY_PARAMS.get(key, None)
            if iso_string:
                queryset = queryset.filter(**{key: parser.parse(iso_string)})
        return queryset

class PointLossDetail(generics.RetrieveAPIView):
    queryset = PointLoss.objects.all()
    serializer_class = PointLossSerializer

class StudentPointLossList(PointLossList):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        queryset = super(StudentPointLossList, self).get_queryset()
        return queryset.filter(periodic_record__student__pk=pk)


class BehaviorIncidentTypeList(generics.ListAPIView):
    queryset = BehaviorIncidentType.objects.all()
    serializer_class = BehaviorIncidentTypeSerializer

class BehaviorIncidentTypeDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncidentType.objects.all()
    serializer_class = BehaviorIncidentTypeSerializer

class StudentBehaviorIncidentTypeList(BehaviorIncidentTypeList):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        queryset = super(StudentBehaviorIncidentTypeList, self).get_queryset()
        return queryset.filter(Q(applicable_student__pk=pk) |
                               Q(applicable_student__isnull=True))

class BehaviorIncidentList(generics.ListAPIView):
    serializer_class = BehaviorIncidentSerializer
    def get_queryset(self):
        queryset = BehaviorIncident.objects.all()
        for key in ('started_at__gt', 'started_at__gte', 'started_at__lte', 'started_at__lt'):
            iso_string = self.request.QUERY_PARAMS.get(key, None)
            if iso_string:
                queryset = queryset.filter(**{key: parser.parse(iso_string)})
        return queryset

class BehaviorIncidentDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncident.objects.all()
    serializer_class = BehaviorIncidentSerializer

class StudentBehaviorIncidentList(BehaviorIncidentList):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        queryset = super(StudentBehaviorIncidentList, self).get_queryset()
        return queryset.filter(student__pk=pk)

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class StudentPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        posts = Post.objects.filter(student__pk=pk)
        return posts

class AttendanceSpanList(generics.ListAPIView):
    serializer_class = AttendanceSpanSerializer

    # TODO: enable PUT functionality

    def get_queryset(self):
        queryset = AttendanceSpan.objects.all()
        for key in ('date', 'date__lt', 'date__lte', 'date__gt', 'date__gte'):
            iso_string = self.request.QUERY_PARAMS.get(key, None)
            if iso_string:
                queryset = queryset.filter(**{key: parser.parse(iso_string).date()})

        return queryset

class AttendanceSpanDetail(generics.RetrieveAPIView):
    queryset = AttendanceSpan.objects.all()
    serializer_class = AttendanceSpanSerializer

class StudentAttendanceSpanList(AttendanceSpanList):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        queryset = super(StudentAttendanceSpanList, self).get_queryset()
        return queryset.filter(student__pk=pk)
