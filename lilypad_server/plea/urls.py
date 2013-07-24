from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^students/$',
        views.StudentList.as_view(), name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$',
        views.StudentDetail.as_view(), name='student-detail'),

    url(r'^students/(?P<pk>[0-9]+)/charts/$',
        views.StudentChartList.as_view(), name='student_chart-list'),
    url(r'^students/(?P<pk>[0-9]+)/behaviortypes/$',
        views.StudentBehaviorIncidentTypeList.as_view(), name='student_behaviortype-list'),
    url(r'^students/(?P<pk>[0-9]+)/behaviorincidents/$',
        views.StudentBehaviorIncidentList.as_view(), name='student_behaviorincident-list'),

    url(r'^behaviorincidents/$',
        views.BehaviorIncidentList.as_view(), name='behaviorincident-list'),
    url(r'^behaviorincidents/(?P<pk>[0-9]+)/$',
        views.BehaviorIncidentDetail.as_view(), name='behaviorincident-detail'),

    url(r'^behaviortypes/$',
        views.BehaviorIncidentTypeList.as_view(), name='behaviorincidenttype-list'),
    url(r'^behaviortypes/(?P<pk>[0-9]+)/$',
        views.BehaviorIncidentTypeDetail.as_view(), name='behaviorincidenttype-detail'),

    url(r'^topics/$',
        views.TopicList.as_view(), name='topic-list'),
    url(r'^topics/(?P<pk>[0-9]+)/$',
        views.TopicDetail.as_view(), name='topic-detail'),

    url(r'^subtopics/(?P<pk>[0-9]+)/$',
        views.SubtopicDetail.as_view(), name='subtopic-detail'),

    url(r'^input_channels/$',
        views.InputChannelList.as_view(), name='inputchannel-list'),
    url(r'^input_channels/(?P<pk>[0-9]+)/$',
        views.InputChannelDetail.as_view(), name='inputchannel-detail'),

    url(r'^output_channels/$',
        views.OutputChannelList.as_view(), name='outputchannel-list'),
    url(r'^output_channels/(?P<pk>[0-9]+)/$',
        views.OutputChannelDetail.as_view(), name='outputchannel-detail'),

    url(r'^charts/$',
        views.ChartList.as_view(), name='chart-list'),
    url(r'^charts/(?P<pk>[0-9]+)/$',
        views.ChartDetail.as_view(), name='chart-detail'),

    url(r'^charts/(?P<pk>[0-9]+)/daymetrics/$',
        views.ChartDayMetricList.as_view(), name='chart_daymetric-list'),
    url(r'^charts/(?P<pk>[0-9]+)/phaselines/$',
        views.ChartPhaseLineList.as_view(), name='chart_phaseline-list'),

    url(r'^daymetrics/$',
        views.DayMetricList.as_view(), name='daymetric-list'),
    url(r'^daymetrics/(?P<pk>[0-9]+)/$',
        views.DayMetricDetail.as_view(), name='daymetric-detail'),

    url(r'^phaselines/$',
        views.PhaseLineList.as_view(), name='phaseline-list'),
    url(r'^phaselines/(?P<pk>[0-9]+)/$',
        views.PhaseLineDetail.as_view(), name='phaseline-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

# in development mode, serve the index page with Django's dev server
if settings.DEBUG:
    urlpatterns += patterns('',
        url('^$', views.index, name='index'),
    )
