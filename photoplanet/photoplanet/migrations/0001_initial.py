# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'photoplanet_photo', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_avatar_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('photo_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('like_count', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'photoplanet', ['Photo'])

        # Adding model 'Vote'
        db.create_table(u'photoplanet_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photoplanet.Photo'])),
            ('vote_value', self.gf('django.db.models.fields.IntegerField')()),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'photoplanet', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'photoplanet_photo')

        # Deleting model 'Vote'
        db.delete_table(u'photoplanet_vote')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'photoplanet.photo': {
            'Meta': {'object_name': 'Photo'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'like_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'user_avatar_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'photoplanet.vote': {
            'Meta': {'object_name': 'Vote'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photoplanet.Photo']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'vote_value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['photoplanet']