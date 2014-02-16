# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'editor_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fn', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sn', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'editor', ['User'])

        # Adding model 'Systems'
        db.create_table(u'editor_systems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'editor', ['Systems'])

        # Adding model 'Case'
        db.create_table(u'editor_case', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300, db_index=True)),
            ('dirTree', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, db_index=True, blank=True)),
            ('information', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('system', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('folder_array', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'editor', ['Case'])

        # Adding model 'FilePath'
        db.create_table(u'editor_filepath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('folder', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'editor', ['FilePath'])

        # Adding M2M table for field case on 'FilePath'
        m2m_table_name = db.shorten_name(u'editor_filepath_case')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('filepath', models.ForeignKey(orm[u'editor.filepath'], null=False)),
            ('case', models.ForeignKey(orm[u'editor.case'], null=False))
        ))
        db.create_unique(m2m_table_name, ['filepath_id', 'case_id'])

        # Adding model 'UserToCase'
        db.create_table(u'editor_usertocase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Case'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.User'])),
        ))
        db.send_create_signal(u'editor', ['UserToCase'])

        # Adding model 'ImageFile'
        db.create_table(u'editor_imagefile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imageFile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('annotations_path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Case'])),
        ))
        db.send_create_signal(u'editor', ['ImageFile'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'editor_user')

        # Deleting model 'Systems'
        db.delete_table(u'editor_systems')

        # Deleting model 'Case'
        db.delete_table(u'editor_case')

        # Deleting model 'FilePath'
        db.delete_table(u'editor_filepath')

        # Removing M2M table for field case on 'FilePath'
        db.delete_table(db.shorten_name(u'editor_filepath_case'))

        # Deleting model 'UserToCase'
        db.delete_table(u'editor_usertocase')

        # Deleting model 'ImageFile'
        db.delete_table(u'editor_imagefile')


    models = {
        u'editor.case': {
            'Meta': {'object_name': 'Case'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            'dirTree': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'case': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['editor.Case']", 'symmetrical': 'False'}),
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