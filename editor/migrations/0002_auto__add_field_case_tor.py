# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Case.tor'
        db.add_column(u'editor_case', 'tor',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 8, 24, 0, 0), max_length=111),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Case.tor'
        db.delete_column(u'editor_case', 'tor')


    models = {
        u'editor.case': {
            'Meta': {'object_name': 'Case'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'system': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'temp': ('django.db.models.fields.CharField', [], {'max_length': '111'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'tor': ('django.db.models.fields.CharField', [], {'max_length': '111'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['editor.User']", 'null': 'True', 'through': u"orm['editor.UserToAuthor']", 'blank': 'True'})
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
        u'editor.usertoauthor': {
            'Meta': {'object_name': 'UserToAuthor'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.Case']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['editor.User']"})
        }
    }

    complete_apps = ['editor']