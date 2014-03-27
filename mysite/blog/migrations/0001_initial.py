# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GImage'
        db.create_table(u'blog_gimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('blog', ['GImage'])

        # Adding model 'Conference'
        db.create_table(u'blog_conference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'blog', ['Conference'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default='0')),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Adding model 'Code'
        db.create_table(u'blog_code', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('git_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('programming_language', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=600, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Code'])

        # Adding model 'Publication'
        db.create_table(u'blog_publication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=220, null=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('bibtex', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('conference_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Conference'])),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')(default=2014)),
        ))
        db.send_create_signal(u'blog', ['Publication'])

        # Adding model 'Project'
        db.create_table(u'blog_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('mtext', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default='0')),
        ))
        db.send_create_signal(u'blog', ['Project'])

        # Adding M2M table for field publications on 'Project'
        m2m_table_name = db.shorten_name(u'blog_project_publications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'blog.project'], null=False)),
            ('publication', models.ForeignKey(orm[u'blog.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'publication_id'])

        # Adding model 'ProjectImage'
        db.create_table(u'blog_projectimage', (
            (u'gimage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['blog.GImage'], unique=True, primary_key=True)),
            ('entity_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Project'])),
        ))
        db.send_create_signal(u'blog', ['ProjectImage'])

        # Adding model 'ProjectVideo'
        db.create_table(u'blog_projectvideo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entity_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Project'])),
            ('link', self.gf('embed_video.fields.EmbedVideoField')(max_length=200, null=True)),
        ))
        db.send_create_signal(u'blog', ['ProjectVideo'])

        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default='0')),
        ))
        db.send_create_signal(u'blog', ['Article'])

        # Adding model 'ArticleImage'
        db.create_table(u'blog_articleimage', (
            (u'gimage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['blog.GImage'], unique=True, primary_key=True)),
            ('entity_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Article'])),
        ))
        db.send_create_signal(u'blog', ['ArticleImage'])

        # Adding model 'CodeSnippet'
        db.create_table(u'blog_codesnippet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('programming_language', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('code', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'blog', ['CodeSnippet'])


    def backwards(self, orm):
        # Deleting model 'GImage'
        db.delete_table(u'blog_gimage')

        # Deleting model 'Conference'
        db.delete_table(u'blog_conference')

        # Deleting model 'Category'
        db.delete_table(u'blog_category')

        # Deleting model 'Code'
        db.delete_table(u'blog_code')

        # Deleting model 'Publication'
        db.delete_table(u'blog_publication')

        # Deleting model 'Project'
        db.delete_table(u'blog_project')

        # Removing M2M table for field publications on 'Project'
        db.delete_table(db.shorten_name(u'blog_project_publications'))

        # Deleting model 'ProjectImage'
        db.delete_table(u'blog_projectimage')

        # Deleting model 'ProjectVideo'
        db.delete_table(u'blog_projectvideo')

        # Deleting model 'Article'
        db.delete_table(u'blog_article')

        # Deleting model 'ArticleImage'
        db.delete_table(u'blog_articleimage')

        # Deleting model 'CodeSnippet'
        db.delete_table(u'blog_codesnippet')


    models = {
        u'blog.article': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Article'},
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.articleimage': {
            'Meta': {'object_name': 'ArticleImage', '_ormbases': ['blog.GImage']},
            'entity_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Article']"}),
            u'gimage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['blog.GImage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'blog.code': {
            'Meta': {'object_name': 'Code'},
            'details': ('django.db.models.fields.TextField', [], {'max_length': '600', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'git_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programming_language': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'blog.codesnippet': {
            'Meta': {'object_name': 'CodeSnippet'},
            'code': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programming_language': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'blog.conference': {
            'Meta': {'object_name': 'Conference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        'blog.gimage': {
            'Meta': {'object_name': 'GImage'},
            'fname': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'blog.project': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Project'},
            'category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtext': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'0'"}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['blog.Publication']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'blog.projectimage': {
            'Meta': {'object_name': 'ProjectImage', '_ormbases': ['blog.GImage']},
            'entity_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Project']"}),
            u'gimage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['blog.GImage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'blog.projectvideo': {
            'Meta': {'object_name': 'ProjectVideo'},
            'entity_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Project']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200', 'null': 'True'})
        },
        u'blog.publication': {
            'Meta': {'object_name': 'Publication'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '220', 'null': 'True'}),
            'bibtex': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'conference_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Conference']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2014'})
        }
    }

    complete_apps = ['blog']