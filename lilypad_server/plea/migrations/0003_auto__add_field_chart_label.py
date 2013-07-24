# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Chart.label'
        db.add_column(u'plea_chart', 'label',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Chart.label'
        db.delete_column(u'plea_chart', 'label')


    models = {
        u'plea.behaviorincident': {
            'Meta': {'object_name': 'BehaviorIncident'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurred_at': ('django.db.models.fields.DateTimeField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'behavior_incidents'", 'to': u"orm['plea.Student']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.BehaviorIncidentType']"})
        },
        u'plea.behaviorincidenttype': {
            'Meta': {'object_name': 'BehaviorIncidentType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'custom_behavior_types'", 'to': u"orm['plea.Student']"})
        },
        u'plea.chart': {
            'Meta': {'object_name': 'Chart'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'input_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.InputChannel']"}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'output_channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.OutputChannel']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.Student']"}),
            'subtopic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.Subtopic']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.Topic']"})
        },
        u'plea.daymetric': {
            'Meta': {'object_name': 'DayMetric'},
            'chart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.Chart']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'plea.inputchannel': {
            'Meta': {'ordering': "('menu_order',)", 'object_name': 'InputChannel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'plea.outputchannel': {
            'Meta': {'ordering': "('menu_order',)", 'object_name': 'OutputChannel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'plea.phaseline': {
            'Meta': {'object_name': 'PhaseLine'},
            'chart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.Chart']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'plea.student': {
            'Meta': {'object_name': 'Student'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'plea.subtopic': {
            'Meta': {'ordering': "('menu_order',)", 'object_name': 'Subtopic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plea.Topic']"})
        },
        u'plea.topic': {
            'Meta': {'ordering': "('menu_order',)", 'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['plea']