from plea.models import Student, BehaviorIncidentType, BehaviorIncident
from plea.models import Topic, Subtopic, InputChannel, OutputChannel
from plea.models import Chart, DayMetric, PhaseLine

from django.contrib import admin

admin.site.register(Student)

admin.site.register(BehaviorIncidentType)
admin.site.register(BehaviorIncident)

admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(InputChannel)
admin.site.register(OutputChannel)

admin.site.register(Chart)
admin.site.register(DayMetric)
admin.site.register(PhaseLine)
