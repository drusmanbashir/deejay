# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field files on 'Case'
        m2m_table_name = db.shorten_name(u'editor_case_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('case', models.ForeignKey(orm[u'editor.case'], null=False)),
            ('filepath', models.ForeignKey(orm[u'editor.filepath'], null=False))
        ))
        db.create_unique(m2m_table_name, ['case_id', 'filepath_id'])

        # Removing M2M table for field case on 'FilePath'
        db.delete_table(db.shorten_name(u'editor_filepath_case'))


    def backwards(self, orm):
        # Removing M2M table for field files on 'Case'
        db.delete_table(db.shorten_name(u'editor_case_files'))

        # Adding M2M table for field case on 'FilePath'
        m2m_table_name = db.shorten_name(u'editor_filepath_case')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('filepath', models.ForeignKey(orm[u'editor.filepath'], null=False)),
            ('case', models.ForeignKey(orm[u'editor.case'], null=False))
        ))
        db.create_unique(m2m_table_name, ['filepath_id', 'case_id'])


    models = {
        u'editor.case': {
            'Meta': {'object_name': 'Case'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            'dirTree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['editor.FilePath']", 'symmetrical': 'False'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'folder_array': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['editor.User']", 'null': 'True', 'through': u"orm['editor.UserToCase']", 'blank': 'True'})
        },
        u'editor.filepath': {
            'Meta': {'object_name': 'FilePath'},
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'editor.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'annotations_path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.Case']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'editor.systems': {
            'Meta': {'object_name': 'Systems'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'editor.user': {
            'Meta': {'object_name': 'User'},
            'fn': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sn': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'editor.usertocase': {
            'Meta': {'object_name': 'UserToCase'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.Case']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.User']"})
        }
    }

    complete_apps = ['editor']