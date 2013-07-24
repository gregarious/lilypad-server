# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'plea_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'plea', ['Student'])

        # Adding model 'BehaviorIncidentType'
        db.create_table(u'plea_behaviorincidenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='custom_behavior_types', to=orm['plea.Student'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'plea', ['BehaviorIncidentType'])

        # Adding model 'BehaviorIncident'
        db.create_table(u'plea_behaviorincident', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.BehaviorIncidentType'])),
            ('started_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('ended_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='behavior_incidents', to=orm['plea.Student'])),
            ('last_modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'plea', ['BehaviorIncident'])

        # Adding model 'Topic'
        db.create_table(u'plea_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('menu_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'plea', ['Topic'])

        # Adding model 'Subtopic'
        db.create_table(u'plea_subtopic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.Topic'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('menu_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'plea', ['Subtopic'])

        # Adding model 'InputChannel'
        db.create_table(u'plea_inputchannel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('menu_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'plea', ['InputChannel'])

        # Adding model 'OutputChannel'
        db.create_table(u'plea_outputchannel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('menu_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'plea', ['OutputChannel'])

        # Adding model 'Chart'
        db.create_table(u'plea_chart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.Topic'])),
            ('subtopic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.Subtopic'])),
            ('input_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.InputChannel'])),
            ('output_channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.OutputChannel'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.Student'])),
        ))
        db.send_create_signal(u'plea', ['Chart'])

        # Adding model 'DayMetric'
        db.create_table(u'plea_daymetric', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('chart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.Chart'])),
        ))
        db.send_create_signal(u'plea', ['DayMetric'])

        # Adding model 'PhaseLine'
        db.create_table(u'plea_phaseline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('chart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plea.Chart'])),
        ))
        db.send_create_signal(u'plea', ['PhaseLine'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'plea_student')

        # Deleting model 'BehaviorIncidentType'
        db.delete_table(u'plea_behaviorincidenttype')

        # Deleting model 'BehaviorIncident'
        db.delete_table(u'plea_behaviorincident')

        # Deleting model 'Topic'
        db.delete_table(u'plea_topic')

        # Deleting model 'Subtopic'
        db.delete_table(u'plea_subtopic')

        # Deleting model 'InputChannel'
        db.delete_table(u'plea_inputchannel')

        # Deleting model 'OutputChannel'
        db.delete_table(u'plea_outputchannel')

        # Deleting model 'Chart'
        db.delete_table(u'plea_chart')

        # Deleting model 'DayMetric'
        db.delete_table(u'plea_daymetric')

        # Deleting model 'PhaseLine'
        db.delete_table(u'plea_phaseline')


    models = {
        u'plea.behaviorincident': {
            'Meta': {'object_name': 'BehaviorIncident'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ended_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {}),
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