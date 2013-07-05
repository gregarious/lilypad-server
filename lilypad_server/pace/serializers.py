from rest_framework import serializers

from pace.models import Student

class StudentSerializer(serializers.ModelSerializer):
    behavior_point_record_collection = serializers.HyperlinkedIdentityField(
        view_name='global_behavior_point_records-list')

    # no tests written yet
    # discussion_collection = serializers.HyperlinkedIdentityField(
    #     view_name='discussion-list')

    class Meta:
        model = Student
        fields = ('first_name', 'last_name',
            'behavior_point_record_collection')
