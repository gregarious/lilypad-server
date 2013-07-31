from pace.models import Student, PeriodicRecord, BehaviorIncidentType, BehaviorIncident
from pace.models import Post, ReplyPost
from django.contrib import admin

admin.site.register(Student)
admin.site.register(PeriodicRecord)
admin.site.register(BehaviorIncidentType)
admin.site.register(BehaviorIncident)

class ReplyInline(admin.TabularInline):
    model = ReplyPost

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ReplyInline
    ]

admin.site.register(Post, PostAdmin)
