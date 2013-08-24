# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserToAuthor'
        db.delete_table(u'editor_usertoauthor')

        # Adding model 'UserToCase'
        db.create_table(u'editor_usertocase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Case'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.User'])),
        ))
        db.send_create_signal(u'editor', ['UserToCase'])


    def backwards(self, orm):
        # Adding model 'UserToAuthor'
        db.create_table(u'editor_usertoauthor', (
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.Case'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['editor.User'])),
        ))
        db.send_create_signal(u'editor', ['UserToAuthor'])

        # Deleting model 'UserToCase'
        db.delete_table(u'editor_usertocase')


    models = {
        u'editor.case': {
            'Meta': {'object_name': 'Case'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['editor.User']", 'null': 'True', 'through': u"orm['editor.UserToCase']", 'blank': 'True'})
        },
        u'editor.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
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