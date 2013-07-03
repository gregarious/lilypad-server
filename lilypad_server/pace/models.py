from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
from django.contrib.auth.models import User

class Classroom(models.Model):
    name = models.CharField(max_length=200)
    teacher_oids = ListField(models.CharField(max_length=24),
        help_text='ObjectID strings for auth.User objects')

    student_oids = ListField(models.CharField(max_length=24),
        help_text='ObjectID strings for pace.Student objects')

    @property
    def teachers(self):
        User.objects.filter(id__in=self.teacher_oids)

    @property
    def students(self):
        Student.objects.filter(id__in=self.student_oids)


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,
        help_text="(or partial last name)")

    discussions = ListField(EmbeddedModelField('Discussion'), editable=False)
    behavior_point_records = ListField(EmbeddedModelField('GlobalBehaviorPointRecord'),
        editable=False)

class Discussion(models.Model):
    title = models.CharField(max_length=200)
    notes = ListField(EmbeddedModelField('Note'), editable=False)

class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    content = models.TextField(blank=True)
    author_oid = models.CharField(max_length=24,
        help_text='ObjectID string for auth.User object')

    @property
    def author(self):
        User.objects.get(id=self.author_oid)


GLOBAL_BEHAVIOR_TYPES = (
    ("UKW", "Use kind words"),
    ("DW", "Do your work"),
    ("FD", "Follow directions"),
    ("BS", "Be safe"),
)

class GlobalBehaviorPointRecord(models.Model):
    behavior_type = models.CharField(max_length=4,
        choices=GLOBAL_BEHAVIOR_TYPES)
    recorded_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    max_value = models.IntegerField(null=True, blank=True)

    date = models.DateField()
    period = models.IntegerField()
