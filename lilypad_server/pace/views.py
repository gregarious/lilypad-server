from pace.models import Student, PeriodicRecord
from pace.models import BehaviorIncidentType, BehaviorIncident

from pace.serializers import StudentSerializer, PeriodicRecordSerializer
from pace.serializers import BehaviorIncidentSerializer, BehaviorIncidentTypeSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from django.http import HttpResponse

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

class BehaviorIncidentTypeList(generics.ListAPIView):
    queryset = BehaviorIncidentType.objects.all()
    serializer_class = BehaviorIncidentTypeSerializer

class BehaviorIncidentTypeDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncidentType.objects.all()
    serializer_class = BehaviorIncidentTypeSerializer

class BehaviorIncidentList(generics.ListAPIView):
    queryset = BehaviorIncident.objects.all()
    serializer_class = BehaviorIncidentSerializer

class BehaviorIncidentDetail(generics.RetrieveAPIView):
    queryset = BehaviorIncident.objects.all()
    serializer_class = BehaviorIncidentSerializer

# # no tests written yet
# # def discussions_list(request, pk):
# #     return HttpResponse('discussions for student %s' %
# #         str(pk))

# # def discussions_detail(request, student_pk, discussion_pk):
# #     return HttpResponse('discussion %s for student %s' %
# #         (str(discussion_pk), str(student_pk)))
