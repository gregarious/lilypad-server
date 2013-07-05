from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^students/$',
        views.StudentList.as_view(), name='student-list'),
    url(r'^students/(?P<pk>[0-9a-f]+)/$',
        views.StudentDetail.as_view(), name='student-detail'),

    url(r'^students/(?P<pk>[0-9a-f]+)/global_behavior_point_records/$',
        views.GlobalBehaviorPointRecordList.as_view(), name='globalbehaviorpointrecord-list'),

    url(r'^students/(?P<student_pk>[0-9a-f]+)/global_behavior_point_records/(?P<pk>[0-9a-f]+)/$',
        views.GlobalBehaviorPointRecordDetail.as_view(), name='globalbehaviorpointrecord-detail'),

    # no tests written yet
    # url(r'^students/(?P<pk>[0-9a-f]+)/discussions/$',
    #     views.discussions_list, name='discussions-list'),
    # url(r'^students/(?P<student_pk>[0-9a-f]+)/discussions/(?P<discussion_pk>[0-9a-f]+)/$',
    #     views.discussions_detail, name='discussions-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
