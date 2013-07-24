from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^students/$',
        views.StudentList.as_view(), name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$',
        views.StudentDetail.as_view(), name='student-detail'),

    url(r'^students/(?P<pk>[0-9]+)/periodicrecords/$',
        views.StudentPeriodicRecordList.as_view(), name='student_periodicrecord-list'),
    url(r'^students/(?P<pk>[0-9]+)/behaviortypes/$',
        views.StudentBehaviorIncidentTypeList.as_view(), name='student_behaviortype-list'),
    url(r'^students/(?P<pk>[0-9]+)/behaviorincidents/$',
        views.StudentBehaviorIncidentList.as_view(), name='student_behaviorincident-list'),

    url(r'^periodicrecords/$',
        views.PeriodicRecordList.as_view(), name='periodicrecord-list'),
    url(r'^periodicrecords/(?P<pk>[0-9]+)/$',
        views.PeriodicRecordDetail.as_view(), name='periodicrecord-detail'),

    url(r'^behaviorincidents/$',
        views.BehaviorIncidentList.as_view(), name='behaviorincident-list'),
    url(r'^behaviorincidents/(?P<pk>[0-9]+)/$',
        views.BehaviorIncidentDetail.as_view(), name='behaviorincident-detail'),

    url(r'^behaviortypes/$',
        views.BehaviorIncidentTypeList.as_view(), name='behaviorincidenttype-list'),
    url(r'^behaviortypes/(?P<pk>[0-9]+)/$',
        views.BehaviorIncidentTypeDetail.as_view(), name='behaviorincidenttype-detail'),

    # no tests written yet
    # url(r'^students/(?P<pk>[0-9a-f]+)/discussions/$',
    #     views.discussions_list, name='discussions-list'),
    # url(r'^students/(?P<student_pk>[0-9a-f]+)/discussions/(?P<discussion_pk>[0-9a-f]+)/$',
    #     views.discussions_detail, name='discussions-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

# in development mode, serve the index page with Django's dev server
if settings.DEBUG:
    urlpatterns += patterns('',
        url('^$', views.index, name='index'),
    )
