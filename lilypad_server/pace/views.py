from django.db.models import Q

from pace.models import Student, PeriodicRecord
from pace.models import BehaviorIncidentType, BehaviorIncident
from pace.models import Post, ReplyPost

from pace.serializers import StudentSerializer, PeriodicRecordSerializer
from pace.serializers import BehaviorIncidentSerializer, BehaviorIncidentTypeSerializer
from pace.serializers import PostSerializer

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
        for key in ('date', 'date__gte', 'date__lt',):
            iso_string = self.request.QUERY_PARAMS.get(key, None)
            if iso_string:
                queryset = queryset.filter(**{key: parser.parse(iso_string).date()})
        return queryset

class PeriodicRecordDetail(generics.RetrieveAPIView):
    queryset = PeriodicRecord.objects.all()
    serializer_class = PeriodicRecordSerializer

class StudentPeriodicRecordList(PeriodicRecordList):
    serializer_class = PeriodicRecordSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        queryset = super(StudentPeriodicRecordList, self).get_queryset()
        return queryset.filter(student__pk=pk)

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
        records = BehaviorIncidentType.objects.filter(
            Q(applicable_student__pk=pk) | Q(applicable_student__isnull=True))
        return records

class BehaviorIncidentList(generics.ListAPIView):
    serializer_class = BehaviorIncidentSerializer
    def get_queryset(self):
        queryset = BehaviorIncident.objects.all()
        for key in ('started_at__gte', 'started_at__lt',):
            iso_string = self.request.QUERY_PARAMS.get(key, None)
            if iso_string:
                queryset = queryset.filter(**{key: parser.parse(iso_string)})
        return queryset

class BehaviorIncidentDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncident.objects.all()
    serializer_class = BehaviorIncidentSerializer

class StudentBehaviorIncidentList(BehaviorIncidentList):
    serializer_class = BehaviorIncidentSerializer

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


# # no tests written yet
# # def discussions_list(request, pk):
# #     return HttpResponse('discussions for student %s' %
# #         str(pk))

# # def discussions_detail(request, student_pk, discussion_pk):
# #     return HttpResponse('discussion %s for student %s' %
# #         (str(discussion_pk), str(student_pk)))
