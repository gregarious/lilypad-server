from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    name = models.CharField(max_length=200)
    staff = models.ManyToManyField(User)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,
        help_text="(or partial last name)")

    classroom = models.ForeignKey(Classroom)

class PeriodicPointRecord(models.Model):
    period = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student)

    is_eligible = models.BooleanField(default=True)

    kind_words_points = models.IntegerField()
    complete_work_points = models.IntegerField()
    follow_directions_points = models.IntegerField()
    be_safe_points = models.IntegerField()

class BehaviorIncidentType(models.Model):
    code = models.CharField(max_length=6, blank=True)
    label = models.CharField(max_length=100)
    supports_duration = models.BooleanField(default=False)

    applicable_student = models.ForeignKey(Student, null=True, blank=True,
        related_name='custom_behavior_types',
        help_text='Set if this type is a custom behavior for a student')

class BehaviorIncident(models.Model):
    type = models.ForeignKey(BehaviorIncidentType)
    started_at = models.DateTimeField()

    ended_at = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(blank=True)

    student = models.ForeignKey(Student)


# class Discussion(models.Model):
#     title = models.CharField(max_length=200)
#     notes = ListField(EmbeddedModelField('Note'), editable=False)

# class Note(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)

#     content = models.TextField(blank=True)
#     author_oid = models.CharField(max_length=24,
#         help_text='ObjectID string for auth.User object')

#     @property
#     def author(self):
#         User.objects.get(id=self.author_oid)
