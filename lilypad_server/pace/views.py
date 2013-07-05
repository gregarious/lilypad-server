from pace.models import Student
from pace.serializers import StudentSerializer, GlobalBehaviorPointRecordSerializer

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

class GlobalBehaviorPointRecordList(APIView):
    def get_student_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_student_object(pk)
        records = student.behavior_point_records
        serializer = GlobalBehaviorPointRecordSerializer(
            records, student_pk=pk, many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        student = self.get_student_object(pk)

        serializer = GlobalBehaviorPointRecordSerializer(
            data=request.DATA,
            student_pk=pk,
            context={'request': request})
        if serializer.is_valid():
            new_record = serializer.save()
            student.behavior_point_records.append(new_record)
            student.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GlobalBehaviorPointRecordDetail(APIView):
    def get_objects(self, student_pk, record_pk):
        try:
            # don't want to access GlobalBehaviorPointRecord table
            student = Student.objects.get(pk=student_pk)
            records = [r for r in student.behavior_point_records if r.id == record_pk]
            return student, records[0]
        except:
            raise Http404

    def get(self, request, student_pk, pk, format=None):
        _, record = self.get_objects(student_pk, pk)
        serializer = GlobalBehaviorPointRecordSerializer(
            record, student_pk=student_pk, context={'request': request})
        return Response(serializer.data)

    def put(self, request, student_pk, pk, format=None):
        student, record = self.get_objects(student_pk, pk)
        serializer = GlobalBehaviorPointRecordSerializer(
            record, data=request.DATA, student_pk=student_pk,
            context={'request': request})
        if serializer.is_valid():
            new_record = serializer.save()
            student.behavior_point_records.append(new_record)
            student.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# no tests written yet
# def discussions_list(request, pk):
#     return HttpResponse('discussions for student %s' %
#         str(pk))

# def discussions_detail(request, student_pk, discussion_pk):
#     return HttpResponse('discussion %s for student %s' %
#         (str(discussion_pk), str(student_pk)))
