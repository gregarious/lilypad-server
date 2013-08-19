from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    name = models.CharField(max_length=200)
    staff = models.ManyToManyField(User, null=True, blank=True)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,
        help_text="(or partial last name)")

    classroom = models.ForeignKey(Classroom, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class PeriodicRecord(models.Model):
    period = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student, related_name='periodic_records')

    is_eligible = models.BooleanField(default=True)

    # these are nullable if not eligible
    kind_words_points = models.IntegerField(null=True, blank=True)
    complete_work_points = models.IntegerField(null=True, blank=True)
    follow_directions_points = models.IntegerField(null=True, blank=True)
    be_safe_points = models.IntegerField(null=True, blank=True)

    last_changed_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '<%s_%d:%s>' % (self.date.strftime('%Y-%m-%d'), self.period, self.student)

    def _decrement(self, attribute):
        current = getattr(self, attribute)
        if current <= 0:
            raise ValueError('Cannot decrement: Value already 0')
        setattr(self, attribute, current-1)

    def declare_point_loss(self, point_type):
        '''
        Decrement a point value and create a record of it with a PointLoss
        object. `point_loss` should be a constant from the POINT_CATEGORIES_*
        choices.

        Returns the new PointLoss object. If value for point_type is already
        0, None will be returned instead. Will raise ValueError if unknown
        type is provided.

        This factory method should be the *only* place PointLoss models are
        created.
        '''
        unknown_type = False
        try:
            if point_type == POINT_CATEGORIES_KW:
                self._decrement('kind_words_points')
            elif point_type == POINT_CATEGORIES_CW:
                self._decrement('complete_work_points')
            elif point_type == POINT_CATEGORIES_FD:
                self._decrement('follow_directions_points')
            elif point_type == POINT_CATEGORIES_BS:
                self._decrement('be_safe_points')
            else:
                unknown_type = True
        except ValueError:
            return None

        if unknown_type:
            raise ValueError('Unsupported point_type: %s' % (str(point_type)))

        return PointLoss.objects.create(periodic_record=self,
            point_type=point_type)


# constant values for point loss type
POINT_CATEGORIES_KW = 'kw'
POINT_CATEGORIES_CW = 'cw'
POINT_CATEGORIES_FD = 'fd'
POINT_CATEGORIES_BS = 'bs'
POINT_CATEGORIES = (
    (POINT_CATEGORIES_KW, 'Kind Words'),
    (POINT_CATEGORIES_CW, 'Complete Work'),
    (POINT_CATEGORIES_FD, 'Follow Directions'),
    (POINT_CATEGORIES_BS, 'Be Safe'),
)
class PointLoss(models.Model):
    occurred_at = models.DateTimeField(auto_now_add=True)
    periodic_record = models.ForeignKey(PeriodicRecord)
    point_type = models.CharField(max_length=4, choices=POINT_CATEGORIES)
    comment = models.TextField(blank=True)

    def __unicode__(self):
        return "<'%s' loss for record #%s @%s>" % (self.point_type, self.periodic_record.id, self.occurred_at.strftime('%Y-%m-%dT%H:%I:%S'),)

class BehaviorIncidentType(models.Model):
    code = models.CharField(max_length=6, blank=True)
    label = models.CharField(max_length=100)
    supports_duration = models.BooleanField(default=False)

    applicable_student = models.ForeignKey(Student, null=True, blank=True,
        related_name='custom_behavior_types',
        help_text='Set if this type is a custom behavior for a student')

    def __unicode__(self):
        if self.applicable_student:
            return '%s (custom: %s)' % (self.label, self.applicable_student)
        else:
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

class BasePost(models.Model):
    class Meta:
        abstract = True
        ordering = ('created_at',)

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    content = models.TextField()

class Post(BasePost):
    student = models.ForeignKey(Student)

class ReplyPost(BasePost):
    parent_post = models.ForeignKey(Post, related_name='replies')
