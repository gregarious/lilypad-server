from django.db.models import Q

from pace.models import Student, PeriodicRecord
from pace.models import BehaviorIncidentType, BehaviorIncident

from pace.serializers import StudentSerializer, PeriodicRecordSerializer
from pace.serializers import BehaviorIncidentSerializer, BehaviorIncidentTypeSerializer

from django.http import Http404
from rest_framework import generics

class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class PeriodicRecordList(generics.ListAPIView):
    queryset = PeriodicRecord.objects.all()
    serializer_class = PeriodicRecordSerializer

class PeriodicRecordDetail(generics.RetrieveAPIView):
    queryset = PeriodicRecord.objects.all()
    serializer_class = PeriodicRecordSerializer

class StudentPeriodicRecordList(generics.ListAPIView):
    serializer_class = PeriodicRecordSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            raise Http404
        records = PeriodicRecord.objects.filter(student__pk=pk)
        return records

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

# # no tests written yet
# # def discussions_list(request, pk):
# #     return HttpResponse('discussions for student %s' %
# #         str(pk))

# # def discussions_detail(request, student_pk, discussion_pk):
# #     return HttpResponse('discussion %s for student %s' %
# #         (str(discussion_pk), str(student_pk)))
