# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GroupPayment'
        db.create_table(u'pennycount_grouppayment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payments_added', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'pennycount', ['GroupPayment'])

        # Adding M2M table for field shared_with on 'GroupPayment'
        db.create_table(u'pennycount_grouppayment_shared_with', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('grouppayment', models.ForeignKey(orm[u'pennycount.grouppayment'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'pennycount_grouppayment_shared_with', ['grouppayment_id', 'user_id'])

        # Adding model 'Group'
        db.create_table(u'pennycount_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='my_groups', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=2048)),
        ))
        db.send_create_signal(u'pennycount', ['Group'])

        # Adding M2M table for field users on 'Group'
        db.create_table(u'pennycount_group_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'pennycount.group'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(u'pennycount_group_users', ['group_id', 'user_id'])

        # Adding model 'Payment'
        db.create_table(u'pennycount_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_payment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pennycount.GroupPayment'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payments', to=orm['auth.User'])),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('paid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'pennycount', ['Payment'])

        # Adding model 'UserPayment'
        db.create_table(u'pennycount_userpayment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_user_payments', to=orm['auth.User'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_user_payments', to=orm['auth.User'])),
            ('value', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'pennycount', ['UserPayment'])

        # Adding unique constraint on 'UserPayment', fields ['from_user', 'to_user']
        db.create_unique(u'pennycount_userpayment', ['from_user_id', 'to_user_id'])

        # Adding model 'Friend'
        db.create_table(u'pennycount_friend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friends', to=orm['auth.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'pennycount', ['Friend'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserPayment', fields ['from_user', 'to_user']
        db.delete_unique(u'pennycount_userpayment', ['from_user_id', 'to_user_id'])

        # Deleting model 'GroupPayment'
        db.delete_table(u'pennycount_grouppayment')

        # Removing M2M table for field shared_with on 'GroupPayment'
        db.delete_table('pennycount_grouppayment_shared_with')

        # Deleting model 'Group'
        db.delete_table(u'pennycount_group')

        # Removing M2M table for field users on 'Group'
        db.delete_table('pennycount_group_users')

        # Deleting model 'Payment'
        db.delete_table(u'pennycount_payment')

        # Deleting model 'UserPayment'
        db.delete_table(u'pennycount_userpayment')

        # Deleting model 'Friend'
        db.delete_table(u'pennycount_friend')


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
        u'pennycount.friend': {
            'Meta': {'object_name': 'Friend'},
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friends'", 'to': u"orm['auth.User']"})
        },
        u'pennycount.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'my_groups'", 'to': u"orm['auth.User']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'belonging_groups'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'pennycount.grouppayment': {
            'Meta': {'object_name': 'GroupPayment'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shared_with': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'group_payments'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payments_added'", 'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'pennycount.payment': {
            'Meta': {'object_name': 'Payment'},
            'group_payment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pennycount.GroupPayment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payments'", 'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'pennycount.userpayment': {
            'Meta': {'unique_together': "(('from_user', 'to_user'),)", 'object_name': 'UserPayment'},
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_user_payments'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_user_payments'", 'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0'})
        }
    }

    complete_apps = ['pennycount']