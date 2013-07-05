from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^students/$',
        views.students_list, name='students-list'),
    url(r'^students/(?P<pk>[0-9a-f]+)$',
        views.students_detail, name='students-detail'),

    url(r'^students/(?P<pk>[0-9a-f]+)/global_behavior_point_records/$',
        views.global_behavior_point_records_list, name='global_behavior_point_records-list'),

    url(r'^students/(?P<student_pk>[0-9a-f]+)/global_behavior_point_records/(?P<record_pk>[0-9a-f]+)/$',
        views.global_behavior_point_records_detail, name='global_behavior_point_records-detail'),

    # no tests written yet
    # url(r'^students/(?P<pk>[0-9a-f]+)/discussions/$',
    #     views.discussions_list, name='discussions-list'),
    # url(r'^students/(?P<student_pk>[0-9a-f]+)/discussions/(?P<discussion_pk>[0-9a-f]+)/$',
    #     views.discussions_detail, name='discussions-detail'),
)
