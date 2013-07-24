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
    occurred_at = models.DateTimeField()

    comment = models.TextField(blank=True)
    student = models.ForeignKey(Student, related_name='behavior_incidents')

    def __unicode__(self):
        return '<%s@%s:%s>' % (self.type.label, self.occurred_at.strftime('%Y-%m-%d %H:%M:%S'), self.student)

class Topic(models.Model):
    class Meta:
        ordering = ('menu_order',)

    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Subtopic(models.Model):
    class Meta:
        ordering = ('menu_order',)

    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s: %s' % (unicode(self.topic), self.name)

class InputChannel(models.Model):
    class Meta:
        ordering = ('menu_order',)

    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class OutputChannel(models.Model):
    class Meta:
        ordering = ('menu_order',)

    name = models.CharField(max_length=30)
    menu_order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Chart(models.Model):
    topic = models.ForeignKey(Topic)
    subtopic = models.ForeignKey(Subtopic)
    input_channel = models.ForeignKey(InputChannel)
    output_channel = models.ForeignKey(OutputChannel)

    label = models.CharField(max_length=100, null=True, blank=True, help_text="additional label for chart")
    student = models.ForeignKey(Student)

    created_at = models.DateTimeField(auto_now_add=True)
    last_opened_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        if not self.label:
            return "%s:%s" % (self.subtopic, self.student)
        else:
            return self.label

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

    def __unicode__(self):
        return '<%s@%s:%s>' % (METRIC_TYPE_CHOICES[self.type], self.occurred_at.strftime('%Y-%m-%d %H:%M:%S'), self.chart)


class PhaseLine(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()

    chart = models.ForeignKey(Chart)

    def __unicode__(self):
        return '<%s@%s:%s>' % (title, self.occurred_at.strftime('%Y-%m-%d %H:%M:%S'), self.chart)
