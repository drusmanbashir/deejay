# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CaseToFile'
        db.create_table(u'editor_casetofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Case'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.FilePath'])),
        ))
        db.send_create_signal(u'editor', ['CaseToFile'])

        # Removing M2M table for field files on 'Case'
        db.delete_table(db.shorten_name(u'editor_case_files'))


    def backwards(self, orm):
        # Deleting model 'CaseToFile'
        db.delete_table(u'editor_casetofile')

        # Adding M2M table for field files on 'Case'
        m2m_table_name = db.shorten_name(u'editor_case_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('case', models.ForeignKey(orm[u'editor.case'], null=False)),
            ('filepath', models.ForeignKey(orm[u'editor.filepath'], null=False))
        ))
        db.create_unique(m2m_table_name, ['case_id', 'filepath_id'])


    models = {
        u'editor.case': {
            'Meta': {'object_name': 'Case'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            'dirTree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['editor.FilePath']", 'null': 'True', 'through': u"orm['editor.CaseToFile']", 'blank': 'True'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'folder_array': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['editor.User']", 'null': 'True', 'through': u"orm['editor.UserToCase']", 'blank': 'True'})
        },
        u'editor.casetofile': {
            'Meta': {'object_name': 'CaseToFile'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.Case']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.FilePath']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'editor.filepath': {
            'Meta': {'ordering': "('path',)", 'object_name': 'FilePath'},
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