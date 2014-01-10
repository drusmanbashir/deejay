# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SBA.date'
        db.delete_column(u'knowledge_sba', 'date')

        # Adding field 'SBA.created'
        db.add_column(u'knowledge_sba', 'created',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2014, 1, 9, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SBA.date'
        db.add_column(u'knowledge_sba', 'date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2014, 1, 9, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'SBA.created'
        db.delete_column(u'knowledge_sba', 'created')


    models = {
        u'knowledge.answer': {
            'Meta': {'object_name': 'Answer'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'correct': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sba': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['knowledge.SBA']"})
        },
        u'knowledge.mnemonic': {
            'Meta': {'object_name': 'Mnemonic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'knowledge.sba': {
            'Meta': {'object_name': 'SBA'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pacscon.Patient']"}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'reference': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'pacscon.diagnosis': {
            'Meta': {'object_name': 'Diagnosis', 'db_table': "u'diagnosis'"},
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'pk'"})
        },
        u'pacscon.patient': {
            'Meta': {'object_name': 'Patient', 'db_table': "u'patient'"},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pacscon.Diagnosis']", 'db_column': "u'diagnosis_fk'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "u'pk'"}),
            'merge_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pacscon.Patient']", 'null': 'True', 'db_column': "u'merge_fk'", 'blank': 'True'}),
            'pat_attrs': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_birthdate': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_custom1': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_custom2': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_custom3': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_fn_sx': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_gn_sx': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_i_name': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_id': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_id_issuer': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_name': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_p_name': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'pat_sex': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['knowledge']