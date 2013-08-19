from pace.models import Student, PeriodicRecord, PointLoss, \
                        BehaviorIncidentType, BehaviorIncident, \
                        Post, ReplyPost, AttendanceSpan
from django.contrib import admin

admin.site.register(Student)
admin.site.register(PeriodicRecord)
admin.site.register(PointLoss)
admin.site.register(BehaviorIncidentType)
admin.site.register(BehaviorIncident)
admin.site.register(AttendanceSpan)

class ReplyInline(admin.TabularInline):
    model = ReplyPost

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ReplyInline
    ]

admin.site.register(Post, PostAdmin)
