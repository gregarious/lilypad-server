from pace.models import Student
from pace.serializers import StudentSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse

def students_list(request):
    s = Student.objects.all()[0]
    ser = StudentSerializer(s)

    return HttpResponse('student list: %s' % str(ser.data))

def students_detail(request, pk):
    return HttpResponse('student %s' % str(pk))

def global_behavior_point_records_list(request, pk):
    return HttpResponse('behaviors for student %s' %
        str(pk))

def global_behavior_point_records_detail(request, student_pk, record_pk):
    return HttpResponse('behavior %s for student %s' %
        (str(record_pk), str(student_pk)))

# no tests written yet
# def discussions_list(request, pk):
#     return HttpResponse('discussions for student %s' %
#         str(pk))

# def discussions_detail(request, student_pk, discussion_pk):
#     return HttpResponse('discussion %s for student %s' %
#         (str(discussion_pk), str(student_pk)))
