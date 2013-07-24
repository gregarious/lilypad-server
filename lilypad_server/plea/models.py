from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,
        help_text="(or partial last name)")
    date_of_birth = models.DateField(null=True, blank=True)

    # TODO: add this
    # classroom = models.ForeignKey(Classroom, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class BehaviorIncidentType(models.Model):
    code = models.CharField(max_length=6, blank=True)
    label = models.CharField(max_length=100)

    student = models.ForeignKey(Student, related_name='custom_behavior_types')
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.label

class BehaviorIncident(models.Model):
    type = models.ForeignKey(BehaviorIncidentType)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)

    comment = models.TextField(blank=True)
    student = models.ForeignKey(Student, related_name='behavior_incidents')

    last_modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '<%s@%s:%s>' % (self.type.label, self.started_at.strftime('%Y-%m-%d %H:%M:%S'), self.student)

class Topic(models.Model):
    class Meta:
        ordering = ('menu_order',)

    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

class Subtopic(models.Model):
    class Meta:
        ordering = ('menu_order',)

    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

class InputChannel(models.Model):
    class Meta:
        ordering = ('menu_order',)

    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

class OutputChannel(models.Model):
    class Meta:
        ordering = ('menu_order',)

    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

class Chart(models.Model):
    topic = models.ForeignKey(Topic)
    subtopic = models.ForeignKey(Subtopic)
    input_channel = models.ForeignKey(InputChannel)
    output_channel = models.ForeignKey(OutputChannel)

    student = models.ForeignKey(Student)

METRIC_TYPE_CHOICES = (
    (0, 'floor'),
    (1, 'corrects'),
    (2, 'errors'),
    (3, 'trials')
)

class DayMetric(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    type = models.IntegerField(choices=METRIC_TYPE_CHOICES)

    chart = models.ForeignKey(Chart)

class PhaseLine(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()

    chart = models.ForeignKey(Chart)
